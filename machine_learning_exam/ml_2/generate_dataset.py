import os
import random

import cv2
import numpy as np
from tqdm import tqdm


def xyxy_to_coco_format(
        x0: float,
        y0: float,
        x1: float,
        y1: float,
        height_px: int,
        width_px: int
) -> tuple:  # xyxy_to_norm_xyhw
    """

    :return:
    """

    height, width = (x1 - x0), (y1 - y0)

    x_center, y_center = x0 + height / 2, y0 + width / 2

    x_center_norm, y_center_norm = x_center / width_px, y_center / height_px
    width_norm, height_norm = width / width_px, height / height_px

    return x_center_norm, y_center_norm, width_norm, height_norm


def add_square(
        image: np.ndarray,
        n_square: int,
        height: int,
        width: int,
        color_bgr: tuple
) -> tuple:

    added_square = set()
    coco_label = []
    for _ in range(n_square):
        thickness = random.randint(1, 3)
        size_side = random.randint(10, 200)  # примерный диапазон, отталкивался от (0.1*height, 0.6*height)

        x0, y0 = random.randint(1, width - size_side - 2), random.randint(1, height - size_side - 2)
        x1, y1 = x0 + size_side, y0 + size_side

        xyxy = (x0, y0, x1, y1)
        if xyxy not in added_square:
            image = cv2.rectangle(image, (x0, y0), (x1, y1), color_bgr, thickness=thickness)
            added_square.add(xyxy)
            coco_label.append(xyxy_to_coco_format(x0 - thickness,
                                                  y0 - thickness,
                                                  x1 + thickness,
                                                  y1 + thickness, height, width))

    return image, coco_label


def add_rectangle(
        image: np.ndarray,
        n_rectangle: int,
        height: int,
        width: int,
        color_bgr: tuple
) -> np.ndarray:

    added_rectangle = set()
    for _ in range(n_rectangle):
        thickness = random.randint(1, 3)
        size_side_0 = random.randint(10 + 1, 200 - 1)
        size_side_1 = random.choice([random.randint(10, size_side_0 - 1), random.randint(size_side_0 + 1, 200)])

        x0, y0 = random.randint(1, width - size_side_0 - 2), random.randint(1, height - size_side_1 - 2)
        x1, y1 = x0 + size_side_0, y0 + size_side_1

        xyxy = (x0, y0, x1, y1)
        if xyxy not in added_rectangle:
            image = cv2.rectangle(image, (x0, y0), (x1, y1), color_bgr, thickness=thickness)
            added_rectangle.add(xyxy)

    return image


def add_circle(
        image: np.ndarray,
        n_circle: int,
        height: int,
        width: int,
        color_bgr: tuple
) -> np.ndarray:

    added_circle = set()
    for _ in range(n_circle):
        thickness = random.randint(1, 3)
        radius = random.randint(10, 100)

        x_center = random.randint(radius - 1, width - radius - 1)
        y_center = random.randint(radius - 1, height - radius - 1)

        xyr = (x_center, y_center, radius)
        if xyr not in added_circle:
            image = cv2.circle(image, (x_center, y_center), radius, color_bgr, thickness)
            added_circle.add(xyr)

    return image


def add_parallelogram(
        image: np.ndarray,
        n_parallelogram: int,
        height: int,
        width: int,
        color_bgr: tuple
) -> np.ndarray:
    """

       (x1,y1) -------- (x2,y2)
             /       /
            /       /
    (x0,y0) -------- (x3,y4)

    :param image:
    :param n_parallelogram:
    :param height:
    :param width:
    :param color_bgr:
    :return:
    """

    is_closed = True
    added_parallelogram = set()
    for _ in range(n_parallelogram):
        thickness = random.randint(1, 3)

        x0, y0 = random.randint(1, width - 50 - 1), random.randint(50 + 1, height - 1)
        x2, y2 = random.randint(x0 + 10, width - 1), random.randint(1, y0 - 10)

        height_paral, width_paral = y0 - y2, x2 - x0
        shift = random.uniform(1/10, 1/4) * width_paral

        x1, y1 = x0 + shift, y2
        x3, y3 = x2 - shift, y0

        xyxys = (x0, y0, x2, y2, shift)
        if xyxys not in added_parallelogram:
            pts = np.array([[x0, y0], [x1, y1], [x2, y2], [x3, y3]], np.int32)
            image = cv2.polylines(image, [pts], is_closed, color_bgr, thickness)
            added_parallelogram.add(xyxys)

    return image
