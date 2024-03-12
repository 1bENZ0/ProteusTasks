import cv2
import numpy


def filled_contour_draw(image: numpy.ndarray, prepared_image: numpy.ndarray,
                        thresh: float = 15,
                        maxval: float = 255,
                        contours_color: tuple[int, int, int] = (0, 0, 255),
                        fill_color: tuple[int, int, int] = (255, 255, 255),
                        thickness: int = 10) -> numpy.ndarray:
    """
    Определяет контуры на предварительно обработанном изображении, рисует контуры с обводкой и заливает их заданным цветом.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    prepared_image : numpy.ndarray
        Предобработанное исходное изображения с контрастной золотой частью.
    thresh : float, default: 15
        Пороговое значение для создания двоичного изображения.
    maxval : float, default: 255
        Максимальное значение для двоичного порога.
    contours_color : tuple, default: (255, 0, 0)
        Кортеж цветов граней контуров.
    fill_color : tuple, default: (255, 255, 255)
        Кортеж цветов заливки контуров.
    thickness : int, default: 10
        Толщина контуров прямоугольника.

    Returns
    -------
    result_image : numpy.ndarray
        Изображение с отрисованными контурами.
    """

    # Преобразование цветового пространства изображения в градацию серого
    gray_contours_image = cv2.cvtColor(prepared_image, cv2.COLOR_BGR2GRAY)

    # Создание бинарного изображения с контурами
    _, threshold_contours = cv2.threshold(gray_contours_image, thresh=thresh,
                                          maxval=maxval,
                                          type=cv2.THRESH_BINARY)

    # Поиск контуров в бинарном изображении
    contours, _ = cv2.findContours(threshold_contours, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    # Создание пустого массива для отрисовки контуров
    contours_only_image = numpy.zeros_like(image)

    # Отрисовка контуров
    cv2.drawContours(contours_only_image, contours, -1, contours_color,
                     thickness=thickness)
    # Заливка контуров
    cv2.fillPoly(contours_only_image, contours, fill_color)

    # Наложение исходного изображения с отрисованными контурами
    result_image = cv2.add(image, contours_only_image)

    return result_image
