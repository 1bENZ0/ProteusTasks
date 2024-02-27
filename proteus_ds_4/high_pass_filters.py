import cv2
import numpy
from show_image import show_image


def canny(image: numpy.ndarray, t_low: float = 19, t_upp: float = 40,
          aperture_size: int = 3, l2gradient: bool = False):
    """
    Фильтр Кэнни для обределения граней на изображении.
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    t_low : float
        Нижний порог для процедуры гистерезиса
    t_upp: float
        Верхний порог для процедуры гистерезиса.
    aperture_size: int
        Размер апертуры для оператора Собеля.
    l2gradient : bool
        Флаг для подсчета градиента. False - используется модуль, True - используется квадрат.

    Returns
    -------
    None
    """
    show_image(cv2.Canny(image, t_low, t_upp, apertureSize=aperture_size,
                         L2gradient=l2gradient), win_name='canny filter')


def laplacian(image: numpy.ndarray, ddepth: int = cv2.CV_64F, ksize: int = 3,
              scale: float = 1, delta: float = 0,
              bordertype: int = cv2.BORDER_DEFAULT):
    """
    Фильтр Лапласа для выделения краев.
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    ddepth : int
        Желаемая глубина конечного изображения.
    ksize : int
        Размер ядра, используемый для расчета фильтров со второй производной.
    scale : float
        Масштабный коэффициент для вычисленных значений Лапласиана.
    delta : float
        Смещение, которое добавляется к результатам перед выводом
    bordertype : int
        Метод экстраполяции пикселей.

    Returns
    -------
    None
    """
    show_image(numpy.uint8(numpy.abs(cv2.Laplacian(image, ddepth, ksize=ksize,
                                                   scale=scale,
                                                   delta=delta,
                                                   borderType=bordertype))),
               win_name='laplacian filter')


def sobel(image: numpy.ndarray, ddepth: int = cv2.CV_64F, ksize: int = 3,
          scale: float = 1, delta: float = 0,
          bordertype: int = cv2.BORDER_DEFAULT):
    """
    Фильтр Собеля для выделения градиентов яркости.
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    ddepth : int
        Желаемая глубина конечного изображения.
    ksize : int
        Размер ядра, используемый для расчета фильтров со второй производной.
    scale : float
        Масштабный коэффициент для вычисленных значений Лапласиана.
    delta : float
        Смещение, которое добавляется к результатам перед выводом
    bordertype : int
        Метод экстраполяции пикселей.


    Returns
    -------
    None
    """
    show_image(cv2.Sobel(src=image, ddepth=ddepth, dx=1, dy=0,
                         ksize=ksize, scale=scale, delta=delta,
                         borderType=bordertype),
               win_name='sobel x')
    show_image(cv2.Sobel(src=image, ddepth=ddepth, dx=0, dy=1,
                         ksize=ksize, scale=scale, delta=delta,
                         borderType=bordertype),
               win_name='sobel y')
    show_image(cv2.Sobel(src=image, ddepth=ddepth, dx=1, dy=1,
                         ksize=ksize, scale=scale, delta=delta,
                         borderType=bordertype),
               win_name='sobel xy')


def scharr(image: numpy.ndarray, ddepth: int = cv2.CV_64F, ksize: int = 3,
           scale: float = 1, delta: float = 0,
           bordertype: int = cv2.BORDER_DEFAULT):
    """
    Фильтр Шарра для выделения градиентов яркости.
    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    ddepth : int
        Желаемая глубина конечного изображения.
    ksize : int
        Размер ядра, используемый для расчета фильтров со второй производной.
    scale : float
        Масштабный коэффициент для вычисленных значений Лапласиана.
    delta : float
        Смещение, которое добавляется к результатам перед выводом
    bordertype : int
        Метод экстраполяции пикселей.


    Returns
    -------
    None
    """
    show_image(cv2.Scharr(src=image, ddepth=ddepth, dx=1, dy=0, scale=scale,
                          delta=delta,
                          borderType=bordertype), win_name='sharr x')
    show_image(cv2.Scharr(src=image, ddepth=ddepth, dx=0, dy=1, scale=scale,
                          delta=delta,
                          borderType=bordertype), win_name='sharr y')
