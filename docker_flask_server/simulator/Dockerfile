FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3","simulator.py"]