import cv2
import torch

X_AXIS = 0
Y_AXIS = 1

RED = (0, 0, 255)

is_object_detected = [0]


def draw_roi(image, mode, color=RED, thickness=2, roi_position=None):
    if roi_position == None:
        if mode == X_AXIS:
            left_line = [(int(0.4 * image.shape[1]), 0), (int(0.4 * image.shape[1]), image.shape[0])]
            right_line = [(int(0.6 * image.shape[1]), 0), (int(0.6 * image.shape[1]), image.shape[0])]
            roi_position = (left_line, right_line)

        elif mode == Y_AXIS:
            upper_line = [(0, int(0.6 * image.shape[0])), (image.shape[1], int(0.6 * image.shape[0]))]
            lower_line = [(0, int(0.8 * image.shape[0])), (image.shape[1], int(0.8 * image.shape[0]))]
            roi_position = (upper_line, lower_line)

    draw_axis(image, roi_position, color, thickness)

    return roi_position

def draw_axis(image, roi_position, color, thickness):
    # line 1 and 2 are left and right lines respectively in x axis
    # line 1 and 2 are upper and lower lines respectively in y axis
    line1, line2 = roi_position[0], roi_position[1]
    cv2.line(image, line1[1], line1[0], color, thickness)
    cv2.line(image, line2[1], line2[0], color, thickness)

