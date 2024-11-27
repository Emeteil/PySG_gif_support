# PySG_gif_support

Очень простая библиотека для поддержки GIF в PySimpleGUI

# Установка
```sh
python -m pip install https://github.com/Emeteil/PySG_gif_support
```
или
```sh
pip install https://github.com/Emeteil/PySG_gif_support
```

# Использование
```python
from PySG_gif_support import *
import PySimpleGUI as sg

layout = [
    [sg.Image(key = "IMAGE")]
]

# ОБЯЗАТЕЛЬНО УКАЗАТЬ finalize = True!!!
window = sg.Window("Test Animation", layout, finalize = True)

thread, stop_event = start_gif_animation(window, "IMAGE", "example_25fps.gif")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

# ОБЯЗАТЕЛЬНО ПЕРЕД ЗАКРЫТИЕМ ОСТАНОВИТЬ АНИМАЦИЮ!!!
stop_gif_animation(stop_event)
window.close()
```