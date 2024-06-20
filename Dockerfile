FROM python:3.10-alpine

RUN apk update
RUN apk add py-pip
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .



EXPOSE 5000

CMD ["python3", "api.py"]


