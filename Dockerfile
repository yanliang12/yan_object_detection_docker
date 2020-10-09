#################################
FROM python:3.5.2

RUN pip install keras==2.1.5
RUN pip install tensorflow==1.6.0

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl

WORKDIR /root/
RUN git clone https://github.com/qqwweee/keras-yolo3.git

WORKDIR /root/keras-yolo3/
RUN wget https://pjreddie.com/media/files/yolov3.weights

RUN pip install h5py
RUN pip install Pillow==7.2.0
RUN pip install matplotlib

RUN python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
RUN python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5

RUN wget https://pjreddie.com/media/files/yolov3-tiny.weights
RUN python convert.py -w yolov3-tiny.cfg yolov3-tiny.weights model_data/tiny_yolo_weights.h5

RUN git clone https://github.com/yanliang12/yan_object_detection_docker.git
RUN mv yan_object_detection_docker/* ./

CMD bash
#################################
