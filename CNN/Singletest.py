
import torch
from torch import nn
from PIL import Image
from torchvision import transforms,datasets 
import cv2
from model import *

class_names = ['Dog','Cat']

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

Mymodel = MyCNN()
Mymodel.load_state_dict(torch.load('./CNN/Result/dogs-vs-cats_vs.pth'))
Mymodel.to(device)
Mymodel.eval()

img_path = './data/cats_00001.jpg'

transform_valid = transforms.Compose([
    transforms.Resize((224,224), interpolation=2),
    transforms.ToTensor()
    ]
)
img = Image.open(img_path)
img_ = transform_valid(img).unsqueeze(0)

img_ = img_.to(device)
outputs = Mymodel(img_)


_, indices = torch.max(outputs,1)
percentage = torch.nn.functional.softmax(outputs, dim=1)[0] * 100
perc = percentage[int(indices)].item()
result = class_names[indices]
print('predicted:', result)
