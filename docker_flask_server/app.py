import logging
import time
from datetime import datetime

from flask import Flask, request, make_response, jsonify

from docker_flask_server.db_models.migrate import make_migrations, get_db_session
from docker_flask_server.db_models.request_logs import Request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logging.info("Waiting for server to start...")
time.sleep(10)
logging.info("Creating tables...")
make_migrations()

session = get_db_session()


@app.route('/', methods=['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def index():
    if request.method is not None:
        resp = {'message': f'{request.method} Request Logged'}
        session.add(Request(method=request.method, host=request.remote_addr, timestamp=datetime.now()))
        session.commit()
        return make_response(jsonify(resp), 200)
