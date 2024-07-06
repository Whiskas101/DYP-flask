FROM python:3.10-alpine

RUN apk update
RUN apk add py-pip
RUN pip install --upgrade pip


WORKDIR /app 

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .



EXPOSE 8000

CMD ["gunicorn","-w","2","-b", "0.0.0.0:8000", "api:app"]


