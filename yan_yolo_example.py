'''
rm yan_yolo.py 
wget https://raw.githubusercontent.com/yanliang12/yan_object_detection_docker/main/yan_yolo.py
'''

from PIL import Image
from yolo import *
from yan_yolo import *

labelme_2_yolo_label(
    train_set_file = '/yan/yan_train.txt',
    converted_train_file = '/yan/yan_train1.txt',
    class_file = '/yan/yan_class.txt'
    )

'''
cp model_data/yolo.h5 /yan/uae_landmark.h5
'''

model = train_yan_yolo_model(
	annotation_path = '/yan/yan_train1.txt',
	classes_path = '/yan/yan_class.txt',
	anchors_path = 'model_data/tiny_yolo_anchors.txt',
	trained_weights_final_file = '/yan/uae_landmark.h5',
	batch_size = 1,
	epochs_fine_tunning = 100,
	pre_trained_weights_path = '/yan/uae_landmark.h5'
	)

yolo_yan = YOLO(**vars(
	model_parameter(
	'/yan/uae_landmark.h5',
	'model_data/tiny_yolo_anchors.txt',
	'/yan/yan_class.txt',
	score = 0.3)))

yan_train = open('/yan/yan_train.txt').read().split('\n')

for f in yan_train:
	print('detecting from {}'.format(f))
	image = Image.open(f)
	r_image = yolo_yan.detect_image(image)
	f1 = re.sub(r'\.', r'_detected.', f)
	r_image.save(f1)
	print()
