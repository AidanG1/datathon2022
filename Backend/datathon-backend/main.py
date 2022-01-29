from flask import Flask, request, jsonify
import convert_to_df
from deta import Deta
import os

# deta = Deta(os.getenv('DETA_PROJECT_KEY')) # configure your Deta project
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'Success!'})

@app.route("/<station>", methods=["GET"])
def get_wspd_by_station(station):
    wspd = convert_to_df.convert_txt_to_df(station).WSPD
    return wspd