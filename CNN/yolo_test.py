import torch
import cv2
from pathlib import Path

# Loading yolo model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Loading image
img = cv2.imread('./data/cats_00001.jpg')

# Predict
results = model(img)

# show result
results.show()

