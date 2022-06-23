from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def index():
    if request.method is not None:
        resp = {'message': f'{request.method} Request Logged'}
        return make_response(jsonify(resp), 200)
