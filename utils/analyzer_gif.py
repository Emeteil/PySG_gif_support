from PIL import Image, ImageSequence
from typing import Union, Generator
import base64
import io, os

def _get_gif_frame_rate(gif_path: Union[str, bytes, os.PathLike]) -> float:
    with Image.open(gif_path) as gif:
        return 1000 / gif.info['duration']

def _gif_to_base64_frames(gif_path: Union[str, bytes, os.PathLike]) -> Generator[str, None, None]:
    gif = Image.open(gif_path)
    
    for frame in ImageSequence.Iterator(gif):
        if frame.mode != 'RGB':
            frame = frame.convert('RGB')
        
        buffer = io.BytesIO()
        frame.save(buffer, format="PNG")
        buffer.seek(0)
        
        frame_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        yield frame_base64