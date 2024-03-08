import cv2
import numpy


def show_image(image: numpy.ndarray, window_width: int = 800,
               window_height: int = 600,
               win_name: str = 'pcb', time: int = 0):
    """
    Функция вывода изображения.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    window_width : int
        Ширина окна с изображением.
    window_height : int
        Высота окна с изображением.
    win_name : str
        Название окна.
    time : int
        Время до закрытия окна в миллисекундах. При 0 ожидает нажатие любой клавиши.

    Returns
    -------
    None
    """
    try:
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(win_name, window_width, window_height)
        cv2.imshow(win_name, image)
        return cv2.waitKey(time)
    except Exception as e:
        raise Exception(f"Ошибка во время отображения: {e}")
