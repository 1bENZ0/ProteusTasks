import cv2
import numpy
from show_image import show_image


def test_numpy_operations(img: numpy.ndarray, scalar: int = 15) -> None:
    """
    Математические операции с матрицей на скаляр

    Parameters
    ----------
    img : numpy.ndarray
        Исходное изображение.
    scalar : int, default: 15
        Скаляр для умножения.

    Returns
    -------
    None
    """
    l, a, b = cv2.split(cv2.cvtColor(img, cv2.COLOR_RGB2LAB))
    show_image(l, time=3000, win_name='L channel without addition')
    l_addition = numpy.clip(numpy.add(l, scalar), 0, 255).astype(numpy.uint8)
    show_image(l_addition, win_name='L channel with addition')

    show_image(l, time=3000, win_name='L channel without subtract')
    l_subtract = numpy.clip(numpy.subtract(l, scalar), 0, 255).astype(
        numpy.uint8)
    show_image(l_subtract, win_name='L channel with subtract')

    show_image(l, time=3000, win_name='L channel without multiply')
    l_multiply = numpy.clip(numpy.multiply(l, scalar), 0, 255).astype(
        numpy.uint8)
    show_image(l_multiply, win_name='L channel with multiply')

    show_image(l, time=3000, win_name='L channel without divide')
    l_divide = numpy.clip(numpy.divide(l, scalar), 0, 255).astype(numpy.uint8)
    show_image(l_divide, win_name='L channel with divide')
