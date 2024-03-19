import cv2

from parse_argument import parse_argument
from change_space_color import test_change_space_color
from split_merge_color import test_split_color, test_merge_color
from numpy_operations import test_numpy_operations
import low_pass_filters
import high_pass_filters
from gold_backing_definition import gold_backing_definition


def main():
    arg = parse_argument()
    try:
        pcb_image = cv2.imread(arg.image)
    except Exception as e:
        raise Exception(f"Ошибка во время загрузки изображения: {e}")
    # # Изменение цветового пространства
    # test_change_space_color(pcb_image)
    # # Разделение на каналы
    # test_split_color(pcb_image)
    # # Обработка канала с помощью Numpy
    # test_numpy_operations(pcb_image)
    # # Объединение в один канал
    # test_merge_color(pcb_image)
    #
    # # Проверка фильтров низких частот
    # low_pass_filters.test_blur(pcb_image)
    # low_pass_filters.test_gaussian_blur(pcb_image)
    # low_pass_filters.test_median_blur(pcb_image)
    # low_pass_filters.test_bilateral_filter(pcb_image)
    #
    # # Проверка фильтров высоких частот
    # high_pass_filters.test_canny(pcb_image)
    # high_pass_filters.test_laplacian(pcb_image)
    # high_pass_filters.test_sobel(pcb_image)
    # high_pass_filters.test_scharr(pcb_image)

    # Определение золотой подложки
    gold_backing_definition(pcb_image)


if __name__ == '__main__':
    main()
