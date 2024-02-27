import cv2

from parse_argument import parse_argument
from change_space_color import change_space_color
from split_merge_color import split_color, merge_color
from numpy_operations import numpy_operations
import low_pass_filters
import high_pass_filters
from gold_backing_definition import gold_backing_definition


def main():
    """
    Main function.
    Returns
    -------
    None
    """
    arg = parse_argument()
    try:
        pcb_image = cv2.imread(arg.image)
    except Exception as e:
        raise Exception(f"Ошибка во время загрузки изображения: {e}")
    # Изменение цветового пространства
    change_space_color(pcb_image)
    # Разделение на каналы
    split_color(pcb_image)
    # Обработка канала с помощью Numpy
    numpy_operations(pcb_image)
    # Объединение в один канал
    merge_color(pcb_image)

    # Проверка фильтров низких частот
    low_pass_filters.blur(pcb_image)
    low_pass_filters.gaussian_blur(pcb_image)
    low_pass_filters.median_blur(pcb_image)
    low_pass_filters.bilateral_filter(pcb_image)

    # Проверка фильтров высоких частот
    high_pass_filters.canny(pcb_image)
    high_pass_filters.laplacian(pcb_image)
    high_pass_filters.sobel(pcb_image)
    high_pass_filters.scharr(pcb_image)

    # Определение золотой подложки
    gold_backing_definition(pcb_image)


if __name__ == '__main__':
    main()
