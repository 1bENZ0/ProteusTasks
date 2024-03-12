import cv2
import numpy


def rectangle_contour_draw(image: numpy.ndarray, prepared_image: numpy.ndarray,
                           thresh: float = 15,
                           maxval: float = 255,
                           color: tuple[int, int, int] = (0, 0, 255),
                           thickness: int = 4) -> numpy.ndarray:
    """
    Определяет контуры на предварительно обработанном изображении, рисует прямоугольники вокруг контуров на исходном изображении.

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
    color : tuple, default: (0, 0, 255)
        Кортеж цветов для контуров прямоугольника.
    thickness : int, default: 4
        Толщина контуров прямоугольника.

    Returns
    -------
    result_image : numpy.ndarray
        Изображение с выделенными прямоугольниками вокруг обнаруженных контуров.
    """

    # Преобразуем изображение в градацию серого
    gray_contours_image = cv2.cvtColor(prepared_image, cv2.COLOR_BGR2GRAY)

    # Создание бинарного изображения с контурами
    _, thresh = cv2.threshold(gray_contours_image, thresh=thresh,
                              maxval=maxval,
                              type=cv2.THRESH_BINARY)

    # Поиск контуров в бинарном изображении
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    # Копирование изображения во избежание изменения исходной информации
    result_image = image.copy()

    # Отрисовка прямоугольников вокруг обнаруженных контуров
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result_image, (x, y), (x + w, y + h), color, thickness)

    return result_image
