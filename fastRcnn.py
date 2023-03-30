#-----------------------------------------------------------------#
# Using fastrcnn_resnet50_fpn
#-----------------------------------------------------------------#

# Loading libraies
import matplotlib.pyplot as plt
import torchvision.transforms as T
from PIL import Image
import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


# Loading pre-traning model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

# Change last layers
num_classes = 2  # numbers of classes(cat and background)
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

# Setting eval model
model.eval()


# Loading image
image = Image.open("data\cats_00001.jpg")

# pre-process image
transform = T.Compose([
    T.Resize(size = (224,224)),
    T.ToTensor(),
    # T.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])
image = transform(image)


# Image --> model
predictions = model([image])

# Get models
boxes = predictions[0]['boxes'].detach().numpy()
scores = predictions[0]['scores'].detach().numpy()
# print(scores.max())


# Show results
# Select the best result
fig, ax = plt.subplots(1)
ax.imshow(image.permute(1, 2, 0))

for box, score in zip(boxes, scores):
    if score == scores.max():
        x1, y1, x2, y2 = box
        w, h = x2 - x1, y2 - y1
        rect = plt.Rectangle((x1, y1), w, h, fill=False, color='red')
        ax.add_patch(rect)

plt.show()
