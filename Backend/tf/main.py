from flask import Flask, jsonify
from deta import Deta
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
@cross_origin()
def index():
    return jsonify({'Success!': 'Yay'})