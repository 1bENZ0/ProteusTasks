import cv2
import numpy
from show_image import show_image


def test_canny(image, t_low, t_upp,
               aperture_size, l2gradient):
    """
    Тест фильтра Кэнни для обределения граней на изображении.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    t_low : float, default: 19
        Нижний порог для процедуры гистерезиса
    t_upp: float, default: 40
        Верхний порог для процедуры гистерезиса.
    aperture_size: int, default: 3
        Размер апертуры для оператора Собеля.
    l2gradient : bool, default: False
        Флаг для подсчета градиента. False - используется модуль, True - используется квадрат.

    Returns
    -------
    None
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_canny = cv2.Canny(image, t_low, t_upp, apertureSize=aperture_size,
                            L2gradient=l2gradient)
    show_image(image_canny, win_name='canny filter')


def test_laplacian(image, ddepth, ksize, scale, delta, bordertype):
    """
    Тест фильтра Лапласа для выделения краев.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    ddepth : int, default: cv2.CV_64F
        Желаемая глубина конечного изображения.
    ksize : int, default: 3
        Размер ядра, используемый для расчета фильтров со второй производной.
    scale : float, default: 1
        Масштабный коэффициент для вычисленных значений Лапласиана.
    delta : float, default: 0
        Смещение, которое добавляется к результатам перед выводом
    bordertype : int, default: cv2.BORDER_DEFAULT
        Метод экстраполяции пикселей.

    Returns
    -------
    None
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_image = cv2.Laplacian(image, ddepth, ksize=ksize,
                                    scale=scale,
                                    delta=delta,
                                    borderType=bordertype)
    show_image(laplacian_image, win_name='laplacian filter')


def test_sobel(image, ddepth, ksize, scale, delta, bordertype):
    """
    Тест фильтра Собеля для выделения градиентов яркости.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    ddepth : int, default: cv2.CV_64F
        Желаемая глубина конечного изображения.
    ksize : int, default: 3
        Размер ядра, используемый для расчета фильтров со второй производной.
    scale : float, default: 1
        Масштабный коэффициент для вычисленных значений Лапласиана.
    delta : float, default: 0
        Смещение, которое добавляется к результатам перед выводом
    bordertype : int, default: cv2.BORDER_DEFAULT
        Метод экстраполяции пикселей.


    Returns
    -------
    None
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_y_image = cv2.Sobel(src=image, ddepth=ddepth, dx=1, dy=0,
                              ksize=ksize, scale=scale, delta=delta,
                              borderType=bordertype)
    show_image(sobel_y_image,
               win_name='sobel x')

    sobel_x_image = cv2.Sobel(src=image, ddepth=ddepth, dx=0, dy=1,
                              ksize=ksize, scale=scale, delta=delta,
                              borderType=bordertype)
    show_image(sobel_x_image,
               win_name='sobel y')

    sobel_xy_image = cv2.Sobel(src=image, ddepth=ddepth, dx=1, dy=1,
                               ksize=ksize, scale=scale, delta=delta,
                               borderType=bordertype)
    show_image(sobel_xy_image,
               win_name='sobel xy')


def test_scharr(image, ddepth, scale, delta, bordertype):
    """
    Тест фильтра Шарра для выделения градиентов яркости.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    ddepth : int, default: cv2.CV_64F
        Желаемая глубина конечного изображения.
    scale : float, default: 1
        Масштабный коэффициент для вычисленных значений Лапласиана.
    delta : float, default: 0
        Смещение, которое добавляется к результатам перед выводом
    bordertype : int, default: cv2.BORDER_DEFAULT
        Метод экстраполяции пикселей.


    Returns
    -------
    None
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharr_x_image = cv2.Scharr(src=image, ddepth=ddepth, dx=1, dy=0,
                               scale=scale,
                               delta=delta,
                               borderType=bordertype)
    show_image(sharr_x_image, win_name='sharr x')

    sharr_y_image = cv2.Scharr(src=image, ddepth=ddepth, dx=0, dy=1,
                               scale=scale,
                               delta=delta,
                               borderType=bordertype)
    show_image(sharr_y_image, win_name='sharr y')
