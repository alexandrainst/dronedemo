FROM rkdigimon/opencv:3.7-4.3.0

RUN apt update && apt install -y curl gnupg ca-certificates zlib1g-dev libjpeg-dev

COPY requirements.* ./

RUN pip install -r requirements.txt

WORKDIR /app

ADD . .

CMD ["python", "main.py", "--model", "detect.tflite", "--labels", "coco_labels.txt"]
