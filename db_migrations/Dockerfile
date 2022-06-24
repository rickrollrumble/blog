# Declare base image to create container
FROM python:3.8-slim-buster



# create new directory at root called /app
WORKDIR /app

# copy contents of current directory to /app
COPY . /app

# install dependencies
RUN python3 -m pip install -r requirements.txt


# run applications
ENTRYPOINT ["python3","migrate.py"]