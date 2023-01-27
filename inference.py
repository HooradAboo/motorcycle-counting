import torch

import cv2
import numpy as np


# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

cap = cv2.VideoCapture('sample_video-2.mp4')

while(cap.isOpened()):
    # Capture each frame
    ret, frame = cap.read()
    if ret == True:
        results = model(frame)
        # print(type(result), result)
# # Images
# img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# # Inference
# results = model(img)

# # Results
results.show()  # or .show(), .save(), .crop(), .pandas(), etc.