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

Verificare se docker necessita dei permessi di root, se li necessita fare:
```
    sudo su
```

Costruire il docker [potrebbe volerci in un po']:
```
    docker build -t facerecognitionimage .
```

Abilitare il video [su X11]:
```
    xhost local:docker
```
oppure se non funzionasse:
```
    xhost +
```

Far partire il docker [la prima volta]:
```
    docker run --name webcam --device /dev/video0:/dev/video0 --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix facerecognitionimage
```

Se il docker è gia presente: 
```
    docker start webcam
```

Fermare il docker:
```
    docker stop webcam
```
