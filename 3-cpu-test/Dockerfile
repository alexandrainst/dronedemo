FROM rkdigimon/opencv:3.7-4.3.0

RUN apt update && apt install -y curl gnupg ca-certificates zlib1g-dev libjpeg-dev && \
    echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt update && apt install python3-edgetpu -y

COPY requirements.* ./

RUN pip install -r requirements.txt

WORKDIR /app

ADD . .

CMD ["python", "main.py", "--model", "detect.tflite", "--labels", "coco_labels.txt"]
