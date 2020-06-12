# Python Camera and TPU via. Docker on macOS, Ubuntu and Raspbian

[![Twitter: @thomasbjgilbert](https://img.shields.io/badge/contact-@thomasbjgilbert-blue.svg?style=flat)](https://twitter.com/thomasbjgilbert)
[![Language: Python](https://img.shields.io/badge/lang-Python-yellow.svg?style=flat)](https://www.python.org/downloads/release/python-370/)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat)](http://opensource.org/licenses/MIT)

## Build
```bash
docker build -t tpu-test .
```

## Run
```bash
docker run --rm -it --privileged -v /dev/bus/usb:/dev/bus/usb tpu-test
```

### Contents
* `main.pu` - analyse camara feed, and output if and where a person is located in the image 