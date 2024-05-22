# Use a base image with Python and OpenCV
FROM python:3.9-slim-bullseye

# Install dependencies, including graphics libraries
RUN apt-get update && \
    apt install -y git \
    build-essential \
    wget \
    unzip \
    libxext6 \
    libxrender1 \
    libxkbcommon-x11-0 \
    libfontconfig1 \
    libgtk2.0-dev \
    pkg-config \
    libglib2.0-0 && \
    apt-get install -y libgl1-mesa-glx && \
    pip install --upgrade pip

# install CMake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.25.1/cmake-3.25.1-linux-x86_64.sh \
    && chmod +x cmake-3.25.1-linux-x86_64.sh \
    && ./cmake-3.25.1-linux-x86_64.sh --skip-license --prefix=/usr/local

# install pip dependencies
RUN pip install opencv-python && \
    pip install dlib && \
    pip install face_recognition

# set path of Qt plugins
#ENV QT_QPA_PLATFORM_PLUGIN_PATH=/usr/local/lib/python3.9/site-packages/cv2/qt/plugins


# set folder to work
RUN mkdir work
WORKDIR work

# Copy the Python script into the container
RUN git clone https://github.com/marcoce005/face_recognition_open_day.git 

WORKDIR face_recognition_open_day/source-code

# Run the Python script
CMD ["python", "main_video.py"]