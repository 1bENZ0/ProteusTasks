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

    # Переводим изображение в другое цветовое пространство
    yuv_image = cv2.cvtColor(pcb_image, code=cv2.COLOR_BGR2YUV)

    # Разделяем изображение на каналы, самый информативный - u канал
    y, u, v = cv2.split(yuv_image)

    # Создаем маску золотых частей платы
    golden_parts_mask = cv2.inRange(u, lowerb=70, upperb=108)

    # Поиск контуров на маске
    contours, _ = cv2.findContours(golden_parts_mask, mode=cv2.RETR_EXTERNAL,
                                   method=cv2.CHAIN_APPROX_SIMPLE)

    # Копируем изображение во избежание изменения исходной информации
    image_for_contours = pcb_image.copy()
    image_for_rectangles = pcb_image.copy()

    # 1 путь - Отрисовка и заливка контуров
    cv2.drawContours(image_for_contours, contours, contourIdx=-1,
                     color=(0, 0, 255),
                     thickness=10)
    cv2.fillPoly(image_for_contours, contours, color=(255, 255, 255))
    show_image(image_for_contours, win_name='image with filled contours')

    # 2 путь - Отрисовка прямоугольников для каждого контура
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_for_rectangles, pt1=(x, y), pt2=(x + w, y + h),
                      color=(0, 0, 255), thickness=4)
    show_image(image_for_rectangles, win_name='image with drown rectangles')


if __name__ == "__main__":
    main()
