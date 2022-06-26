# Declare base image to create container
FROM python:3.8-slim-buster

# expose container port
EXPOSE 7000

# create new directory at root called /app
WORKDIR /app

COPY . /app/docker_flask_server

# install dependencies
RUN python3 -m pip install -r docker_flask_server/requirements.txt

# run applications
ENTRYPOINT ["gunicorn","docker_flask_server.app:app","--bind","0.0.0.0:7000"]