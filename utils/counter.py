import cv2
import torch

X_AXIS = 0
Y_AXIS = 1

RED = (0, 0, 255)

is_object_detected = [0]


def draw_roi(image, mode, color=RED, thickness=2, roi_position=None):
    if roi_position == None:
        if mode == X_AXIS:
            roi_position = [(int(0.4 * image.shape[1]), 0), 
                            (int(0.6 * image.shape[1]), 0), 
                            (int(0.4 * image.shape[1]), image.shape[0]), 
                            (int(0.6 * image.shape[1]), image.shape[0])]

        elif mode == Y_AXIS:
            roi_position = [(0, int(0.6 * image.shape[0])), 
                            (image.shape[1], int(0.6 * image.shape[0])), 
                            (0, int(0.8 * image.shape[0])), 
                            (image.shape[1], int(0.8 * image.shape[0]))]

    draw_axis(image, roi_position, color, thickness)

    return roi_position

def draw_axis(image, roi_position, color, thickness):
    cv2.rectangle(image, roi_position[0], roi_position[3], color, thickness)

