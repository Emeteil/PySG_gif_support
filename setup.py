from setuptools import setup, find_packages

setup(
    name = "PySG_gif_support",
    version = "0.15",
    description = "Очень простая библиотека для поддержки GIF в PySimpleGUI",
    author = "Emeteil",
    author_email = "vorobievdima43@gmail.com",
    packages = find_packages(),
    install_requires = [
        "Pillow",
        "typing",
        "PySimpleGUI"
    ],
    python_requires = ">=3.6",
    package_data = {
        "": ["*.gif"]
    },
    include_package_data = True,
)