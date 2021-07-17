# yan_object_detection_docker

## docker

### pull the docker 

```bash
docker pull yanliang12/yan_object_detection:1.0.1
```

### or build the docker

```bash
docker build -t yan_object_detection:1.0.1 .
```

### rund the docker 

```bash
docker run -it -v /Users/yan/Downloads/:/yan/ yan_object_detection:1.0.1
```


## run the example

```bash
python yan_yolo_example.py
```

<img src="https://raw.githubusercontent.com/yanliang12/yan_object_detection_docker/main/burj_al_arab3_detected.jpeg" height="300"> <img src="https://raw.githubusercontent.com/yanliang12/yan_object_detection_docker/main/burj_khalifa4_detected.jpg" height="300">
