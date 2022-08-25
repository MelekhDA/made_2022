"""
Check some pictures with their labels
"""

import os
from random import choices

import cv2
from PIL import Image

COCO_FORMAT = [
    'class', 'x_center', 'y_center', 'width', 'height'
]


def generate_collect_name(dataset_path: str, count: int) -> list:
    """
    Get list of object names

    :param dataset_path: path to dataset with two packages: "images", "labels"
    :param count: number of random objects from dataset

    :return: list of object names (without .jpg for image or .txt for label)
    """

    all_collect_image = os.listdir(fr'{dataset_path}/images')
    random_collect_name = [
        '.'.join(img_name.split('.')[:-1])
        for img_name in choices(all_collect_image, k=count)
    ]

    return random_collect_name


def read_label(path_label: str) -> list:
    """
    Read *.txt-file with COCO-labels

    :param path_label: path to file with label(s)

    :return:
        list of dict: [
            {'class': 0, 'x_center': 0.33, 'y_center': 0.22, 'width': 0.3, 'height': 0.2},
            ...
        ]
    """

    with open(path_label, 'r') as fio:
        collect_label = [
            dict(zip(COCO_FORMAT, row.rstrip().split()))
            for row in fio.readlines()
        ]

    keys_str_to_float = COCO_FORMAT[1:]
    for dict_label in collect_label:
        for key in keys_str_to_float:
            dict_label[key] = float(dict_label[key])

    return collect_label


def image_with_label(path_picture: str, path_label: str) -> tuple:
    """
    Get image with label box

    https://github.com/ultralytics/yolov5/issues/2293

    :param path_picture:
    :param path_label:

    :returns: (
        filename,
        image
    )

    """

    collect_label = read_label(path_label)

    img = cv2.imread(path_picture)
    image = Image.open(path_picture)
    width_px, height_px = image.size

    out = None

    for dict_label in collect_label:
        x_center_norm, y_center_norm = dict_label['x_center'], dict_label['y_center']
        width_norm, height_norm = dict_label['width'], dict_label['height']

        x_center, y_center = x_center_norm * width_px, y_center_norm * height_px
        width, height = width_norm * width_px, height_norm * height_px

        x, y = x_center - width / 2, y_center - height / 2

        x, y = round(x), round(y)  # min()
        width, height = round(width), round(height)

        out = cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), thickness=1)

    filename = os.path.basename(path_picture)

    if out is not None:
        return filename, out

    return filename, img
