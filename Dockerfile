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
RUN python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5

RUN pip3 install Pillow==7.2.0
RUN pip3 install matplotlib

RUN wget https://raw.githubusercontent.com/yanliang12/yan_object_detection_docker/main/cat.jpg
RUN wget https://raw.githubusercontent.com/yanliang12/yan_object_detection_docker/main/person_and_bike.jpg

CMD bash
#################################
