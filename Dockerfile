FROM python:3.10-slim-buster
WORKDIR /var/www
RUN apt-get update
RUN apt-get install libgl1 -y && apt-get install tesseract-ocr-por -y
RUN python -m pip install --upgrade pip
COPY requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt