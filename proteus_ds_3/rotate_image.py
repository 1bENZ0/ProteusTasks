import cv2
import numpy


def rotate_image(image: numpy.ndarray, angle: int) -> numpy.ndarray:
    """
    Функция для поворота изображения на указанный угол угол.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    angle : int
        Угол поворота.

    Returns
    -------
    numpy.ndarray
    Повернутое изображение
    """
    try:
        height, width = image.shape[:2]
        center_x, center_y = width // 2, height // 2
        rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle,
                                                  1.0)
    except Exception as e:
        raise Exception(f"Ошибка во время поворота изображения: {e}")
    return cv2.warpAffine(image, rotation_matrix, (width, height))
