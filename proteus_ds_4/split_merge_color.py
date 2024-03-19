import cv2
import numpy

from show_image import show_image


def test_split_color(img: numpy.ndarray) -> None:
    """
    Функция разделения изображения на каналы цвета.

    Parameters
    ----------
    img : numpy.ndarray
        Исходное изображение.

    Returns
    -------
    None
    """
    r, g, b = cv2.split(img)
    show_image(r, win_name='red', window_width=400, window_height=300,
               time=500)
    show_image(g, win_name='green', window_width=400, window_height=300,
               time=500)
    show_image(b, win_name='blue', window_width=400, window_height=300,
               time=500)


def test_merge_color(img: numpy.ndarray) -> None:
    """
    Функция объединения каналов для получения изображения

    Parameters
    ----------
    img : numpy.ndarray
        Исходное изображение.

    Returns
    -------
    None
    """
    r, g, b = cv2.split(img)
    show_image(r, win_name='red', window_width=400, window_height=300,
               time=500)
    show_image(g, win_name='green', window_width=400, window_height=300,
               time=500)
    show_image(b, win_name='blue', window_width=400, window_height=300,
               time=500)
    show_image(cv2.merge([r, g, b]), window_width=400, window_height=300,
               win_name='Merged image')
