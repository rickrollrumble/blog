import logging
import random
import socket
from time import sleep

import requests

PROJECT_NAME = "docker_flask_server"

methods = ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']
api_url = f"http://{PROJECT_NAME}-flask_server-1:7000"

logging.basicConfig(level=logging.INFO,
                    filename=f'logs/{socket.gethostbyname(socket.gethostname())}_responses.log')

while True:
    sleep(random.randint(5, 10))
    method_type_index = random.randint(0, len(methods) - 1)
    response = requests.request(methods[method_type_index], api_url)
    logging.log(level=logging.INFO, msg=response.text)
