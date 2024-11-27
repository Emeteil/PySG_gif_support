from setuptools import setup, find_packages

setup(
    name = 'PySG_gif_support',
    version = '0.1',
    description = 'Библиотека для поддержки GIF в PySimpleGUI',
    author = 'Emeteil',
    author_email = 'vorobievdima43@gmail.com',
    packages = find_packages(),
    install_requires = [
        'Pillow',
        'typing',
        'base64',
        'io',
        'PySimpleGUI'
    ],
    python_requires = '>=3.6',
)