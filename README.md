# face_recognition_open_day

## Clonare la repository
```
    git clone https://github.com/marcoce005/face_recognition_open_day.git
    cd face_recognition_open_day
```

## Docker
Se non è presente installare docker [Debian]:
```
    sudo apt install docker.io
```

Costruire il docker [potrebbe volerci in un po']:
```
    docker build -t faceRecognitionImage .
```

Far partire il docker [la prima volta]:
```
    docker run --name webcam --device /dev/video0:/dev/video0 --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix faceRecognitionImage
```

Se il docker è gia presente: 
```
    docker start webcam
```

Fermare il docker:
```
    docker stop webcam
```