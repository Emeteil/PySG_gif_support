from utils.analyzer_gif import _get_gif_frame_rate, _gif_to_base64_frames
import PySimpleGUI as sg
from typing import Union
import time, os, io
import threading
import sys

def start_gif_animation(window: sg.Window, image_key: str, gif_path: Union[str, bytes, os.PathLike], print_author: bool = True) -> threading.Thread:
    """Запускает GIF анимацию

    Args:
        window (sg.Window): Окно PySimpleGUI
        image_key (str): Ключь на sg.Image
        gif_path (Union[str, bytes, os.PathLike]): Путь к .gif файлу
        print_author (bool): 

    Returns:
        threading.Thread: _description_
    """
    def _animate_gif() -> None:
        try:
            frame_rate: float = _get_gif_frame_rate(gif_path)
            frames = _gif_to_base64_frames(gif_path)
            
            while not stop_event.is_set() and window.TKroot.winfo_exists():
                start_time = time.time()

                try:
                    frame_base64 = next(frames)
                    window[image_key].update(data = frame_base64)
                except StopIteration:
                    frames = _gif_to_base64_frames(gif_path)
                    frame_base64 = next(frames)
                    window[image_key].update(data = frame_base64)

                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / frame_rate) - elapsed_time)
                time.sleep(sleep_time)
        except Exception: return
    
    if print_author:
        print("Вы используете библиотеку PySG_gif_support от \033]8;;https://github.com/Emeteil\033\\Emeteil\033]8;;\033\\!")
    
    stop_event = threading.Event()
    thread = threading.Thread(target = _animate_gif)
    thread.start()
    
    return thread, stop_event

def stop_gif_animation(stop_event: threading.Event, exit_program: bool = True) -> None:
    """Останавливает GIF анимацию

    Args:
        stop_event (threading.Event): stop_event который вернул start_gif_animation
        exit_program (bool, optional): Если окно уже закрылось. Defaults to True.
    """
    if exit_program:
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()
    stop_event.set()

if __name__ == "__main__":
    layout = [
        [sg.Image(key = "IMAGE")]
    ]
    
    # ОБЯЗАТЕЛЬНО УКАЗАТЬ finalize = True!!!
    window = sg.Window("Test Animation", layout, finalize = True)
    
    thread, stop_event = start_gif_animation(window, "IMAGE", "example.gif")
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    
    # ОБЯЗАТЕЛЬНО ПЕРЕД ЗАКРЫТИЕМ ОСТАНОВИТЬ АНИМАЦИЮ!!!
    stop_gif_animation(stop_event)
    window.close()