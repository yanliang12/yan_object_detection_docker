############test.py########
import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

yolo = YOLO()

image = Image.open('cat.jpg')
r_image = yolo.detect_image(image)
r_image.save('cat_detected.jpg')

image = Image.open('person_and_bike.jpg')
r_image = yolo.detect_image(image)
r_image.save('person_and_bike_detected.jpg')
############test.py########
