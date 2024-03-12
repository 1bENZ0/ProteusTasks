import cv2
import numpy


def preprocessing(image: numpy.ndarray, ksize=1) -> numpy.ndarray:
    """
    Функция для выделения золотой подложки на фото.

    Parameters
    ----------
    image : numpy.ndarray
        Исходное изображение.
    ksize: int, default: 1
        Размер ядра для оператора Собеля.

    Returns
    -------
    contrast_enhanced_image_with_mask : numpy.ndarray
        Предобработанной изображение.
    """

    def increase_contrast_with_mask(image: numpy.ndarray, mask: numpy.ndarray,
                                    alpha: float = 1.5,
                                    beta: float = 0) -> numpy.ndarray:
        """
        Функция увеличения контраста.

        Parameters
        ----------
        image : numpy.ndarray
            Исходное изображение.
        mask : numpy.ndarray
            Маска по которой происходит увеличение контраста.
        alpha : float, default: 1.5
            Масштабный коэффициент.
        beta : float, default: 0
            Смещение.

        Returns
        -------
        image : numpy.ndarray
            Преобразованное изображение.
        """
        # Увеличение контраста в тех местах где маска не равна нулю.
        image[mask != 0] = cv2.convertScaleAbs(image[mask != 0], alpha=alpha,
                                               beta=beta)
        return image

    # Преобразование входного изображения из цветового пространства BGR в YUV
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # Вычисление градиента по осям x и y, используя оператор Собеля
    gradient_x_image = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=1, dy=0,
                                 ksize=ksize)
    gradient_y_image = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=0, dy=1,
                                 ksize=ksize)

    # Преобразование изображения градиентов в беззнаковые 8-битные целые числа, для дальнейшей работы с инструментами cv2
    gradient_x_image = cv2.convertScaleAbs(gradient_x_image)
    gradient_y_image = cv2.convertScaleAbs(gradient_y_image)

    # Объединение представления градиентов в одно изображение с равными весами
    combined_xy = cv2.addWeighted(gradient_x_image, 0.5, gradient_y_image, 0.5,
                                  0)

    # Создание нижней и верхней границы в цветовом пространстве YUV
    lower_golden_treshold = numpy.array([5, 125, 2], dtype="uint8")
    upper_golden_treshold = numpy.array([30, 255, 255], dtype="uint8")

    # Вывод пикселей изображения которые удовлетворяют границам
    golden_mask = cv2.inRange(cv2.cvtColor(combined_xy, cv2.COLOR_BGR2YUV),
                              lower_golden_treshold, upper_golden_treshold)

    # Увеличение контраста в местах золотой подложки, для более четкого отображения
    contrast_enhanced_image_with_mask = increase_contrast_with_mask(
        combined_xy,
        golden_mask, alpha=3,
        beta=4)

    return contrast_enhanced_image_with_mask
