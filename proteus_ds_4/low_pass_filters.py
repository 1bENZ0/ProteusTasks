import cv2
import numpy
import numpy as np
from show_image import show_image


def blur(image: numpy.ndarray, kernel_size: tuple[int, int] = (100, 100)):
    """
    Размытие изображения используя нормализованный бокс фильтр(линейный).
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение
    kernel_size : tuple[int, int]
        Размер ядра для свертки.

    Returns
    -------
    None
    """
    # Создание ядра для размытия
    kernel = np.ones(kernel_size, dtype=np.float32) / (
            kernel_size[0] * kernel_size[1])
    # Нормализация ядра
    kernel = kernel / np.sum(kernel)
    # Умножения ядра на изображение
    blured_image = cv2.filter2D(image, -1, kernel)

    show_image(blured_image.astype(np.uint8), win_name='self-made blur',
               time=2000)
    show_image(cv2.blur(image, kernel_size), win_name='cv2 blur')


def gaussian_blur(image: numpy.ndarray, kernel_size: int = 101,
                  sigma: float = 0):
    """
    Размытие по Гауссу, используя формулу для вычисления ядра Гаусса.
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение
    kernel_size : int
        Размер ядра для размытия, должен быть положительным и нечетным.
    sigma : float
        Стандартное отклонения.

    Returns
    -------
    None
    """
    # Вычисление сигмы для функции Гаусса по умолчанию
    if sigma <= 0:
        sigma = 0.3 * ((kernel_size - 1) * 0.5 - 1) + 0.8
    # Вычисление ядра Гаусса для заданного размера
    if (kernel_size % 2 == 1) and kernel_size >= 0:
        gauss_kernel = np.fromfunction(
            lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * np.exp(-(
                    (x - (kernel_size - 1) / 2) ** 2 + (
                    y - (kernel_size - 1) / 2) ** 2) / (2 * sigma ** 2)),
            (kernel_size, kernel_size)
        )
    else:
        return print(
            'Ошибка: Размер ядра должен быть четным и не отрицательным')
    # Нормализация ядра
    gauss_kernel = gauss_kernel / np.sum(gauss_kernel)
    # Умножение ядра Гаусса на изображение
    gauss_blured_image = cv2.filter2D(image, -1, gauss_kernel)

    show_image(gauss_blured_image, win_name='self-made gaussian blur',
               time=2000)
    show_image(cv2.GaussianBlur(image, (kernel_size, kernel_size), 0),
               win_name='cv2 gaussian blur')


def median_blur(image: numpy.ndarray, kernel_size: int = 101):
    """
    Медианное размытие. Вычисляет для центра ядра медиану всех пикселей.
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    kernel_size: int
        Размер ядра для размытия, должен быть положительным и нечетным.

    Returns
    -------
    None
    """
    show_image(cv2.medianBlur(image, kernel_size), win_name='cv2 median blur')


def bilateral_filter(image: numpy.ndarray, d: int = 26, sigmacolor: float = 75,
                     sigmaspace: float = 75):
    """
    Применяет билатеральный фильтр к изображению для размытия, сохраняя рёбра.
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    d : float
        Диаметр окрестности каждого пикселя, который используется при фильтрации.
    sigmacolor
        Отклонение фильтра в цветовом пространстве.
    sigmaspace
        Отклонение фильтра в пространстве координат
    Returns
    -------
    None
    """
    show_image(cv2.bilateralFilter(image, d=d, sigmaColor=sigmacolor,
                                   sigmaSpace=sigmaspace),
               win_name='cv2 bilateral filter')
