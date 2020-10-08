import sys
from yolo import YOLO, detect_video
from PIL import Image
from yan_yolo import *

'''
train_yan_yolo_model(
annotation_path = '/yan/yan_train.txt',
classes_path = '/yan/yan_class.txt',
anchors_path = 'model_data/yolo_anchors.txt',
trained_weights_stage_1 = 'trained_weights_stage_1.h5',
batch_size = 32
)
'''

annotation_path = 'train.txt'
classes_path = 'model_data/voc_classes.txt'
anchors_path = 'model_data/yolo_anchors.txt'
trained_weights_final_file = None
trained_weights_stage_1 = 'trained_weights_stage_1.h5'
batch_size = 32
epochs_stage_1 = 10
epochs_fine_tunning = 10

annotation_path = '/yan/yan_train.txt'
classes_path = '/yan/yan_class.txt'
anchors_path = 'model_data/yolo_anchors.txt'
trained_weights_stage_1 = '/yan/trained_weights_stage_1.h5'
trained_weights_final_file = '/yan/trained_weights_final.h5'
batch_size = 1

class Foo:
  def __init__(self):
    self.model_path = '/yan/trained_weights_stage_1.h5'
    self.classes_path = '/yan/yan_class.txt'

object = Foo()

yolo =  YOLO(**vars(object))

image = Image.open('/yan/burj_khalifa1.jpeg')
r_image = yolo.detect_image(image)
r_image.save('/yan/burj_khalifa1_result.jpeg')
