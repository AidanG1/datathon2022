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
    data, mlr = mlr2.mlr(df)
    coefs = mlr.coef_
    points_to_predict = 80
    data_list
    for i in range(points_to_predict):
        previous_row = df[len(df) - 1]
        prev_wspd = mlr.predict(previous_row)
        df.loc[len(df.index)] = {'DateTime': previous_row.DateTime.timedelta(), 'WSPD': prev_wspd}
        df['SMA60'] = df['WSPD'].rolling(60).mean().shift(1)
        df['SMA30'] = df['WSPD'].rolling(30).mean().shift(1)
        df['SMA10'] = df['WSPD'].rolling(10).mean().shift(1)
        df['SMA5'] = df['WSPD'].rolling(5).mean().shift(1)
        df['SMA3'] = df['WSPD'].rolling(3).mean().shift(1)
        df['SMA1'] = df['WSPD'].rolling(1).mean().shift(1)
    for index, row in tswspd.iterrows():
        data_list.append({'datetime': row['DateTime'], 'wspd': row['WSPD']})
    data_dict = {'data': data_list}
    # print(data_dict)
    return jsonify(data_dict)