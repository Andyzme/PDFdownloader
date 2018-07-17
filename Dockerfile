FROM python:3.7.0

WORKDIR /opt/pdf_downloader

COPY . ./

RUN pip install -r requirements.txt
