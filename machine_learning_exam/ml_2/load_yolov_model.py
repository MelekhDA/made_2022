import torch


def load_model(dir_yolov_repo: str,
               path: str,
               iou: float = None,
               confidence: float = None) -> torch.nn.Module:
    """
    Load Yolov5 model from local package
    model - see machine_learning_exam.ml_2.ultralytics_yolov5_master_min.models.common.AutoShape

    :param dir_yolov_repo: directory of yolov5 project (e.x. from github)
    :param path: path to file with weights of neural network (*.pt)
    :param iou: Intersection over Union (IoU) for object detection
    :param confidence: confidence from 0 to 1 for yolov model

    :return: model
    """

    model = torch.hub.load(dir_yolov_repo, 'custom', path=path, source='local', verbose=False)

    print('Before:')
    print(model.conf)  # confidence threshold (0-1)  0.25
    print(model.iou, end='\n' * 2)  # NMS IoU threshold (0-1)  0.45

    if isinstance(confidence, float) and (1 >= confidence >= 0):
        model.conf = confidence

    if isinstance(iou, float) and (1 >= iou >= 0):
        model.iou = iou

    print('After:')
    print(model.conf)
    print(model.iou)

    return model
