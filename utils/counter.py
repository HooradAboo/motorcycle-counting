import cv2
import torch

X_AXIS = 0
Y_AXIS = 1

RED = (0, 0, 255)

is_object_detected = [0]


def draw_roi(image, mode, color=RED, thickness=2, roi_position=None):
    if roi_position == None:
        if mode == X_AXIS:
            roi_position = [int(0.4 * image.shape[1]),  # left
                            0,                          # top
                            int(0.6 * image.shape[1]),  # right
                            image.shape[0]]             # bottom

        elif mode == Y_AXIS:
            roi_position = [0,                          # left
                            int(0.4 * image.shape[0]),  # top
                            image.shape[1],             # right
                            int(0.6 * image.shape[0])]  # bottom

    draw_axis(image, roi_position, color, thickness)

    return roi_position

def draw_axis(image, roi_position, color, thickness):
    cv2.rectangle(image, (roi_position[0], roi_position[1]), (roi_position[2], roi_position[3]), color, thickness)


def get_box_parameter(box):
    left, top, right, bottom = (torch.tensor(box).view(1, 4)).view(-1).tolist()
    # calculate center of box
    center = (int((right - left)/2 + left), int((bottom - top)/2 + top))

    return center, (left, top, right, bottom)


def object_position(image, box, roi_position, mode=0):
    center, _ = get_box_parameter(box)
    is_inside = False

    if (    center[0] > roi_position[0] and
            center[0] < roi_position[2] and
            center[1] > roi_position[1] and
            center[1] < roi_position[3]
        ):
        is_inside = True
        color = (0, 0, 255)
    else:
        color = (255, 0, 0)

    cv2.circle(image, center, 2, color, 2)
    
    return is_inside