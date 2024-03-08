import cv2
import numpy
import numpy as np
from show_image import show_image


def test_blur(image, kernel_size):
    """
    Тест размытия изображения используя нормализованный бокс фильтр(линейный).

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение
    kernel_size : tuple[int, int], default: (100, 100)
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

    cv2_blured_image = cv2.blur(image, kernel_size)
    show_image(cv2_blured_image, win_name='cv2 blur')


def test_gaussian_blur(image, kernel_size, sigma):
    """
    Тест размытия по Гауссу, используя формулу для вычисления ядра Гаусса.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение
    kernel_size : int, default: 101
        Размер ядра для размытия, должен быть положительным и нечетным.
    sigma : float, default: 0
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

    cv2_gaussian_blur = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    show_image(cv2_gaussian_blur,
               win_name='cv2 gaussian blur')


def test_median_blur(image, kernel_size):
    """
    Тест медианного размытия. Вычисляет для центра ядра медиану всех пикселей.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    kernel_size: int, default: 101
        Размер ядра для размытия, должен быть положительным и нечетным.

    Returns
    -------
    None
    """
    median_blur_image = cv2.medianBlur(image, kernel_size)
    show_image(median_blur_image, win_name='cv2 median blur')


def test_bilateral_filter(image, d, sigmacolor, sigmaspace):
    """
    Тест билатерального фильтра к изображению для размытия, сохраняя рёбра.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    d : float, default: 26
        Диаметр окрестности каждого пикселя, который используется при фильтрации.
    sigmacolor : float, default: 75
        Отклонение фильтра в цветовом пространстве.
    sigmaspace : float, default: 75
        Отклонение фильтра в пространстве координат
    Returns
    -------
    None
    """
    bilateral_filter_image = cv2.bilateralFilter(image, d=d,
                                                 sigmaColor=sigmacolor,
                                                 sigmaSpace=sigmaspace)
    show_image(bilateral_filter_image,
               win_name='cv2 bilateral filter')
