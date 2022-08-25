import os
import shutil

from sklearn.model_selection import train_test_split


def create_package_wo_except(path: str, is_log: bool = True):
    """
    Create package without exception if it exist

    :param path: path with new package
    :param is_log: display information about created files in terminal
    """

    try:
        os.makedirs(path)

        if is_log:
            print(f'Directory created: {path}')
    except FileExistsError:
        if is_log:
            print(f'Directory exists: {path}')


def generate_train_val_test(path_from: str, path_to: str, random_state: int) -> None:
    """
    Split dataset by train, val, test

    :param path_from: path to load (dataset)
    :param path_to: path to save (train/val/test dataset)
    :param random_state: random_state

    :return: None
    """

    txt_file_labels = os.listdir(f'{path_from}/labels')

    image_file_names = [f'{i[:-4]}.png' for i in txt_file_labels]

    x_train_val, x_test, y_train_val, y_test = train_test_split(image_file_names, txt_file_labels, test_size=0.2,
                                                                random_state=random_state)
    x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.25, random_state=42)

    create_package_wo_except(fr'{path_to}/train/images')
    create_package_wo_except(fr'{path_to}/train/labels')
    create_package_wo_except(fr'{path_to}/val/images')
    create_package_wo_except(fr'{path_to}/val/labels')
    create_package_wo_except(fr'{path_to}/test/images')
    create_package_wo_except(fr'{path_to}/test/labels')

    for img_name, labels_name in zip(x_train, y_train):
        try:
            shutil.copy(f'{path_from}/images/{img_name}', f'{path_to}/train/images/{img_name}')
            shutil.copy(f'{path_from}/labels/{labels_name}', f'{path_to}/train/labels/{labels_name}')
        except FileNotFoundError as exc:
            print(str(exc))
    print('Train done')

    for img_name, labels_name in zip(x_val, y_val):
        try:
            shutil.copy(f'{path_from}/images/{img_name}', f'{path_to}/val/images/{img_name}')
            shutil.copy(f'{path_from}/labels/{labels_name}', f'{path_to}/val/labels/{labels_name}')
        except FileNotFoundError as exc:
            print(str(exc))
    print('Val done')

    for img_name, labels_name in zip(x_test, y_test):
        try:
            shutil.copy(f'{path_from}/images/{img_name}', f'{path_to}/test/images/{img_name}')
            shutil.copy(f'{path_from}/labels/{labels_name}', f'{path_to}/test/labels/{labels_name}')
        except FileNotFoundError as exc:
            print(str(exc))
    print('Test done')

