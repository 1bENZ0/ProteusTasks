import numpy


def test_blur(image: numpy.ndarray,
              kernel_size: tuple[int, int] = (100, 100)) -> None: ...


def test_gaussian_blur(image: numpy.ndarray, kernel_size: int = 101,
                       sigma: float = 0) -> None: ...


def test_median_blur(image: numpy.ndarray, kernel_size: int = 101) -> None: ...


def test_bilateral_filter(image: numpy.ndarray, d: int = 26,
                          sigmacolor: float = 75,
                          sigmaspace: float = 75) -> None: ...
