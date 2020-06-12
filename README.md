# OpenCV - EdgeTPU - Object Detection - Drones

[![Twitter: @thomasbjgilbert](https://img.shields.io/badge/contact-@thomasbjgilbert-blue.svg?style=flat)](https://twitter.com/thomasbjgilbert)
[![Language: Python](https://img.shields.io/badge/lang-Python-yellow.svg?style=flat)](https://www.python.org/downloads/release/python-370/)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat)](http://opensource.org/licenses/MIT)

This is repository will provide a framework for using OpenCV with an Edge TPU such as [Coral.ai](https://coral.ai/products/accelerator) for use both in develpment and deployment. It has been made in such a way, that you can develope and test with ease on your local machine - and use Docker to deploy on your hardware like for example the Raspbery Pi.

## Drone Support
 This framework is specifically tuned to work in a microservice environment, providing new capabilities to Drones using the [ROS](https://robots.ros.org) ecosystem. 

## Hardware / Software
This framework has been tested to run on the
* [Raspberry Pi 3 Model B+ Rev 1.3](https://www.raspberrypi.org/products/raspberry-pi-3-model-a-plus/)
* [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
* [Macbook Pro 2018](https://www.apple.com/macbook-pro/)

Running these different OS's
* Ubuntu 20.04
* Raspbian 2020-02-13 armhf
* Raspbian 2020-02-13 aarch64
* macOS Catalina 10.15.04

Using various cameras
* [PLAYSTATION Eye](https://en.wikipedia.org/wiki/PlayStation_Eye)
* [Raspberry Pi Camera Module v2](https://www.raspberrypi.org/products/camera-module-v2/)
* Facetime Camera
* Lenovo Thinkvision Camera X1

## Premise
The idea is to provide tools for you to develop your own applications, using these examples to get you going - faster. There are some very good guides, how-to's and tutorials that you can use if you want to read more.
* [Containerizing a Tensorflow Lite Edge-TPU ML Application with Hardware Access on Raspbian](https://cxlabs.sap.com/2019/10/07/containerizing-a-tensorflow-lite-edge-tpu-ml-application-with-hardware-access-on-raspbian/)
* [Benchmarking Edge Computing](https://medium.com/@aallan/benchmarking-edge-computing-ce3f13942245)
* [Detect Objects Using Your Webcam](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/camera.html)
* [Docker Machine with USB support on Windows/macOS](http://gw.tnode.com/docker/docker-machine-with-usb-support-on-windows-macos/)
* [Building Multi-Arch Images for Arm and x86 with Docker Desktop](https://www.docker.com/blog/multi-arch-images/)

## Note on Raspberry Pi
To use the [Raspberry Pi Camera Module v2](https://www.raspberrypi.org/products/camera-module-v2/) on the Rasbery Pi as a standard USB camera, you must first load the driver using the modprobe command
```bash
sudo modprobe bcm2835-v4l2
```
or add `bcm2835-v4l2` to `/etc/modules`. This will expose the camera as a video device on `/dev/video0`.

## Note on Docker
We have provided a set of multi-arch docker images as a baseline that provide the needed OpenCV and Numpy libraries. Feel free to use you own, but the process of esablishing baseline images is very involved. The images can be found here.
* [Python 3.8 with OpenCV 4.2.0](https://hub.docker.com/repository/docker/rkdigimon/opencv)
* [Python 3.8 with OpenCV 4.3.0](https://hub.docker.com/repository/docker/rkdigimon/opencv)
* [Python 3.7 with OpenCV 4.2.0](https://hub.docker.com/repository/docker/rkdigimon/opencv)
* [Python 3.7 with OpenCV 4.3.0](https://hub.docker.com/repository/docker/rkdigimon/opencv)

## Folder Structure
The repository is a set of demonstrators, use them for testing your setup.

    .
    ├── 1-usbcam-test             # Test that your camera is attached, and usable through Docker
    ├── 2-python-test             # Test that OpenCV is able to reach your camera, also through Docker
    ├── 3-cpu-test                # Test that OpenCV works, tensorflow works, also though Docker
    ├── 4-tpu-test                # Test that OpenCV works, and the Edge TPU device works, also though Docker
    ├── LICENSE
    └── README.md

# Development on your machine
If you want to develope your software without having to worry about Docker, you must follow the guides nessecary for setting up e.g. Python, the Coral USB adapter, OpenCV etc. for your specific operating system. Once you are satisfied you can then build the docker image containing your code, and deploy it on your Raspberry Pi or drone.

# Funding
This project is Financed in part by the Institutional and Educational Support Administration.
[Smart monitering af infrastruktur og miljø (digiMON)](https://bedreinnovation.dk/smart-monitering-af-infrastruktur-og-miljø-digimon)