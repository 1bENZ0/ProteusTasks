import numpy
import cv2


def test_canny(image: numpy.ndarray, t_low: float = 19, t_upp: float = 40,
               aperture_size: int = 3, l2gradient: bool = False) -> None: ...


def test_laplacian(image: numpy.ndarray, ddepth: int = cv2.CV_64F,
                   ksize: int = 5,
                   scale: float = 0.2, delta: float = 25,
                   bordertype: int = cv2.BORDER_DEFAULT) -> None: ...


def test_sobel(image: numpy.ndarray, ddepth: int = cv2.CV_64F, ksize: int = 5,
               scale: float = 0.2, delta: float = 25,
               bordertype: int = cv2.BORDER_DEFAULT) -> None: ...


def test_scharr(image: numpy.ndarray, ddepth: int = cv2.CV_64F,
                scale: float = 0.2, delta: float = 25,
                bordertype: int = cv2.BORDER_DEFAULT) -> None: ...
