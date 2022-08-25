import numpy as np


def bgr_to_white_black_color(image: np.ndarray) -> np.ndarray:
    """
    Change color of image

    :param image: bgr image (from cv2.imread(...))

    :return: image with only white and black pixels
    """

    new_image = image.copy()

    new_image[(new_image != 0) & (new_image != 255)] = 0

    return new_image
