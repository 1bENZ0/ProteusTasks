import cv2

from parse_argument import parse_argument
from show_image import show_image
from rotate_image import rotate_image


def main():
    arg = parse_argument()
    try:
        pcb_image = cv2.imread(arg.image)
    except Exception as e:
        raise Exception(f"Ошибка во время загрузки изображения: {e}")

    # Вывод изображения
    show_image(pcb_image)
    print(f"Изображение: \n{pcb_image}",
          f"\nРазрешение : {pcb_image.shape[1]} x {pcb_image.shape[0]}",
          f"\nКоличество каналов: {pcb_image.shape[-1] if pcb_image.ndim == 3 else 1}")

    # Изменение разрешения изображения
    resized_img = cv2.resize(pcb_image, (100, 100))

    # Вывод изображения с новым разрешением
    show_image(resized_img, win_name='resized_image')
    print(
        f"\nНовое разрешение : {resized_img.shape[1]} x {resized_img.shape[0]}")
    pcb_image_copy = pcb_image.copy()

    # Поворот изображение на 45, 90, 180
    show_image(rotate_image(pcb_image_copy, 45), win_name='image_rotated_45')
    show_image(rotate_image(pcb_image_copy, 90), win_name='image_rotated_90')
    show_image(rotate_image(pcb_image_copy, 180), win_name='image_rotated_180')

    # Отображение по горизонтали и вертикали
    show_image(cv2.flip(pcb_image_copy, 0), win_name='horizontal_flip')
    show_image(cv2.flip(pcb_image_copy, 1), win_name='vertical_flip')

    # Выделение области 100 * 100
    cropped_image = pcb_image[1500:1600, 1500:1600]
    show_image(cropped_image, win_name='cropped_image')

    # Изменение значения центрального пикселя
    central_pixel = cropped_image[50, 50]
    print("\nЗначение центрального пикселя: ", central_pixel)
    cropped_image[50, 50] = (0, 0, 255)
    show_image(cropped_image, win_name='cropped_image_with_pixel')

    # Выделение произвольной области
    cropped_image[30:70, 20:80] = (150, 98, 17)
    show_image(cropped_image, win_name='cropped_image_with_area')

    # Отрисовка прямоугольника
    cv2.rectangle(cropped_image, (20, 30), (80, 70), (0, 0, 255), 1)
    cv2.putText(cropped_image, 'rect', (25, 30 - 5), 5, 1, (255, 255, 255), 1)
    show_image(cropped_image, win_name='cropped_image_with_rect')

    # Сохранение изображения
    cv2.imwrite('data/save/cropped_pcb.png', cropped_image)


if __name__ == '__main__':
    main()
