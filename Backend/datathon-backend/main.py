from flask import Flask, request, jsonify
import convert_to_df, mlr2
from deta import Deta
import numpy as np
from flask_cors import CORS, cross_origin

# deta = Deta(os.getenv('DETA_PROJECT_KEY'))
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def index():
    return jsonify({'Success!': 'Yay'})


@app.route("/s/<station>", methods=["GET"])
@cross_origin()
def get_wspd_by_station(station):
    tswspd = convert_to_df.convert_txt_to_df(station)
    data_list = []
    for index, row in tswspd.iterrows():
        data_list.append({'datetime': row['DateTime'], 'wspd': row['WSPD']})
    data_dict = {'data': data_list}
    # print(data_dict)
    return jsonify(data_dict)

@app.route("/mlr2/<station>", methods=["GET"])
@cross_origin()
def get_mlr2_by_station(station):
    df = convert_to_df.convert_txt_to_df(station)
    mlr = mlr2.mlr(df)
    coefs = mlr.coef_
    
    data_list = []
    for index, row in tswspd.iterrows():
        data_list.append({'datetime': row['DateTime'], 'wspd': row['WSPD']})
    data_dict = {'data': data_list}
    # print(data_dict)
    return jsonify(data_dict)