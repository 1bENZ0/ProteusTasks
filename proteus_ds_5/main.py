import cv2
from show_image import show_image
from parse_argument import parse_argument


def main():
    arg = parse_argument()
    try:
        pcb_image = cv2.imread(arg.image)
    except Exception as e:
        raise Exception(f"Ошибка во время загрузки изображения: {e}")
    show_image(pcb_image)

    # Подбор цветового пространства, чтобы подложка была контрастна к окружению
    pcb_image = cv2.cvtColor(pcb_image, cv2.COLOR_BGR2YUV)
    Y, U, V = cv2.split(pcb_image)

    # Наиболее информативный канал - U
    show_image(U, win_name='most informative channel')

    # Создание маски
    pcb_image = cv2.inRange(U, 48, 107)
    show_image(pcb_image, win_name='mask')

    # Выбор и фильтрование контуров
    contours, _ = cv2.findContours(pcb_image, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    min_contour_area = 8000
    max_contour_area = 10000
    filtered_contours = [cnt for cnt in contours if
                         min_contour_area < cv2.contourArea(
                             cnt) < max_contour_area]

    # Отрисовка контуров
    output_image = cv2.drawContours(pcb_image, filtered_contours, -1,
                                    (0, 255, 0),
                                    thickness=cv2.FILLED)

    pcb_image = cv2.fillPoly(output_image, filtered_contours, (0, 255, 0))
    show_image(pcb_image, win_name='pcb image localization')


if __name__ == "__main__":
    main()
