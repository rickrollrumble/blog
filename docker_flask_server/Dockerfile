# Declare base image to create container
FROM python:3.8-alpine

# expose container port
EXPOSE 7000

# create new directory at root called /app
WORKDIR /app

# copy contents of current directory to /app
COPY . /app

# install dependencies
RUN pip3 install -r requirements.txt

# run applications
ENTRYPOINT ["gunicorn","app:app","--bind","0.0.0.0:7000"]