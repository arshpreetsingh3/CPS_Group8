from IPython import display
display.clear_output()

import torch
import ultralytics
ultralytics.checks()

from ultralytics import YOLO
from IPython.display import display, Image

print(torch.cuda.is_available())


yolo task=detect mode=train model=yolov8x.pt data=data.yaml epochs=25 imgsz= 320 plots=True
yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=data.yaml
