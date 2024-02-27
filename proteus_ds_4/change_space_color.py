import numpy as np
import cv2

from show_image import show_image


def change_space_color(img):
    """
    Смена цветового пространства изображения.
    Parameters
    ----------
    img : numpy.ndarray
        Исходное изображение.

    Returns
    -------
    None
    """
    color_spaces = ['BGR', 'RGB', 'XYZ', 'HSV', 'HLS', 'LAB', 'LUV', 'YUV',
                    'CMYK']
    for color_space in color_spaces:

        if color_space == 'RGB':
            show_image(img, win_name='RGB')
            continue

        if color_space == 'CMYK':
            converted_img = img.astype(np.float64) / 255.
            k = 1 - np.max(converted_img, axis=2)
            c = (1 - converted_img[..., 2] - k) / (1 - k)
            m = (1 - converted_img[..., 1] - k) / (1 - k)
            y = (1 - converted_img[..., 0] - k) / (1 - k)
            cmyk_image = (np.dstack((c, m, y, k)) * 255).astype(np.uint8)
            show_image(cmyk_image, win_name='CMYK')
            continue

        converted_img = cv2.cvtColor(img,
                                     getattr(cv2, f'COLOR_RGB2{color_space}'))
        show_image(converted_img, win_name=color_space)
