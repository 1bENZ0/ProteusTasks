import cv2 as cv


def show_image(image, window_width=800, window_height=600, win_name='pcb'):
    """
    Функция вывода изображения.

    Parameters
    ----------
    image : numpy.ndarray[int]
        Исходное изображение.
    window_width : int
        Ширина окна с изображением.
    window_height : int
        Высота окна с изображением.
    win_name : str
        Название окна.

    Returns
    -------
    None
    """
    try:
        cv.namedWindow(win_name, cv.WINDOW_NORMAL)
        cv.resizeWindow(win_name, window_width, window_height)
        cv.imshow(win_name, image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except Exception as e:
        raise Exception(f"Ошибка во время отображения: {e}")


def rotate_image(image, angle: int):
    """
    Функция для поворота изображения на указанный угол угол.

    Parameters
    ----------
    image : numpy.ndarray[int]
        Исходное изображение.
    angle : int
        Угол поворота.

    Returns
    -------
    numpy.ndarray[int]
    """
    try:
        height, width = image.shape[:2]
        center_x, center_y = width // 2, height // 2
        rotation_matrix = cv.getRotationMatrix2D((center_x, center_y), angle,
                                                 1.0)
        return cv.warpAffine(image, rotation_matrix, (width, height))
    except Exception as e:
        raise Exception(f"Ошибка во время поворота изображения: {e}")


pcb_image = cv.imread('data/images/pcb.jpg')

# Вывод изображения
show_image(pcb_image)

print(f"Изображение: \n{pcb_image}",
      f"\nРазрешение : {pcb_image.shape[1]} x {pcb_image.shape[0]}",
      f"\nКоличество каналов: {pcb_image.shape[2]}")

# Изменение разрешения изображения
resized_img = cv.resize(pcb_image, (100, 100))

# Вывод изображения с новым разрешением
show_image(resized_img, win_name='resized_image')
print(f"\nНовое разрешение : {resized_img.shape[1]} x {resized_img.shape[0]}")

pcb_image_copy = pcb_image.copy()

# Поворот изображение на 45, 90, 180
show_image(rotate_image(pcb_image_copy, 45), win_name='image_rotated_45')
show_image(rotate_image(pcb_image_copy, 90), win_name='image_rotated_90')
show_image(rotate_image(pcb_image_copy, 180), win_name='image_rotated_180')

# Отображение по горизонтали и вертикали
show_image(cv.flip(pcb_image_copy, 0), win_name='horizontal_flip')
show_image(cv.flip(pcb_image_copy, 1), win_name='vertical_flip')

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
cv.rectangle(cropped_image, (20, 30), (80, 70), (0, 0, 255), 1)
cv.putText(cropped_image, 'rect', (25, 30 - 5), 5, 1, (255, 255, 255), 1)
show_image(cropped_image, win_name='cropped_image_with_rect')

# Сохранение изображения
cv.imwrite('data/save/cropped_pcb.png', cropped_image)
