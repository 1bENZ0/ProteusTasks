import cv2

from show_image import show_image
from parse_argument import parse_argument
from rectangle_contour_draw import rectangle_contour_draw
from filled_contour_draw import filled_contour_draw
from preprocessing_image import preprocessing


def main():
    arg = parse_argument()
    try:
        pcb_image = cv2.imread(arg.image)
        pcb_contur_image = preprocessing(pcb_image)
    except Exception as e:
        raise Exception(f"Ошибка во время загрузки изображения: {e}")

    image_with_filled_contours = filled_contour_draw(pcb_image,
                                                     pcb_contur_image)
    show_image(image_with_filled_contours,
               win_name='image with filled contours')

    image_with_drown_rectangles = rectangle_contour_draw(pcb_image,
                                                         pcb_contur_image)
    show_image(image_with_drown_rectangles,
               win_name='image with drown rectangles')


if __name__ == "__main__":
    main()
