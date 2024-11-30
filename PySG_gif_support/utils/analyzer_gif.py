from PIL import Image, ImageSequence
from typing import Union, Generator
import io, os

def _get_gif_frame_rate(gif_path: Union[str, bytes, os.PathLike]) -> float:
    with Image.open(gif_path) as gif:
        return 1000 / (gif.info['duration'] if gif.info['duration'] else 40)

def _gif_to_base64_frames(gif_path: Union[str, bytes, os.PathLike]) -> Generator[str, None, None]:
    gif = Image.open(gif_path)
    
    for frame in ImageSequence.Iterator(gif):
        if frame.mode != 'RGB':
            frame = frame.convert('RGB')
        
        buffer = io.BytesIO()
        frame.save(buffer, format="PNG")
        buffer.seek(0)
        
        yield buffer.read()