'''
rm yan_yolo.py 
wget https://raw.githubusercontent.com/yanliang12/yan_object_detection_docker/main/yan_yolo.py
'''

from PIL import Image
from yolo import *
from yan_yolo import *

labelme_2_yolo_label(
    train_set_file = 'yan_train.txt',
    converted_train_file = 'yan_train_annotated.txt',
    class_file = 'yan_class.txt'
    )

model = train_yan_yolo_model(
	annotation_path = 'yan_train_annotated.txt',
	classes_path = 'yan_class.txt',
	anchors_path = 'model_data/tiny_yolo_anchors.txt',
	trained_weights_final_file = 'uae_landmark.h5',
	batch_size = 1,
	epochs_fine_tunning = 50,
	pre_trained_weights_path = 'model_data/tiny_yolo_weights.h5'
	)

yolo_yan = YOLO(**vars(
	model_parameter(
	'uae_landmark.h5',
	'model_data/tiny_yolo_anchors.txt',
	'yan_class.txt',
	score = 0.3)))

yan_train = open('yan_train.txt').read().strip().split('\n')
for f in yan_train:
	print('detecting from {}'.format(f))
	image = Image.open(f)
	r_image = yolo_yan.detect_image(image)
	f1 = re.sub(r'\.', r'_detected.', f)
	r_image.save(f1)
	print()
