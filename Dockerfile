FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install libgl1-mesa-glx tesseract-ocr -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]
