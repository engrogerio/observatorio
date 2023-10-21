#!/bin/bash
cd
git clone https://github.com/raspberrypi/libcamera-apps.git
cd libcamera-apps
mkdir build
cd build
cmake .. -DENABLE_DRM=1 -DENABLE_X11=1 -DENABLE_QT=1 -DENABLE_OPENCV=1 -DENABLE_TFLITE=0
make -j4  # use -j2 on Pi 3 or earlier devices
sudo make install
sudo ldconfig /usr/local/lib # this is only necessary on the first build
