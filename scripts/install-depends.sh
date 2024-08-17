#!/bin/bash

# Gstreamer dependencies
sudo apt-get install \
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools \
    gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 gstreamer1.0-pulseaudio

# setting up system level python packages 
sudo apt-get update
sudo apt-get install python3-dev python3-gi python3-gi-cairo gir1.2-gtk-3.0
sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
sudo sudo apt update
sudo apt install python3-gi

# Last resort
# pip3 install PyGObject --break-system-packages