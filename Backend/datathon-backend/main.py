from flask import Flask, request, jsonify
import convert_to_df
import datetime
import random
import tf, markov
from deta import Deta
import numpy as np
from flask_cors import CORS, cross_origin

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


@app.route('/p/<station>/<date>', methods=['GET'])
@cross_origin()
def get_polar(station, date):
    df = convert_to_df.convert_txt_to_df(station)
    df = df.set_index('DateTime')
    split_date = date.split('-')
    start_date = datetime.datetime(
        int(split_date[0]), int(split_date[1]), int(split_date[2]), 0)
    end_date = datetime.datetime(
        int(split_date[0]), int(split_date[1]), int(split_date[2]), 23)
    df = df.loc[start_date:end_date]
    df = df.reset_index()
    data_list = []
    for index, row in df.iterrows():
        data_list.append(
            {'datetime': row['DateTime'], 'wspd': row['WSPD'], 'wdir': row['WDIR']})
    data_dict = {'data': data_list}
    # print(data_dict)
    return jsonify(data_dict)

@app.route('/pred/<station>', methods=['GET'])
@cross_origin()
def get_predictions(station):
    df = convert_to_df.convert_txt_to_df(station)['WDIR'][:-14].to_list()
    data_list = markov.predict(72, df)
    return jsonify({'data': data_list})

@app.route('/tf/<station>', methods=['GET'])
@cross_origin()
def get_speed_predictions(station):
    data = tf.get_data(station)

    return jsonify({'data': data})


# @app.route("/mlr2/<station>", methods=["GET"])
# @cross_origin()
# def get_mlr2_by_station(station):
#     df = convert_to_df.convert_txt_to_df(station)
#     data, mlr = mlr2.mlr(df)
#     # coefs = mlr.coef_
#     points_to_predict = 80
#     data_list = []
#     for i in range(points_to_predict):
#         previous_row = data[len(data) - 1]
#         pred_wspd = mlr.predict(previous_row)
#         data.loc[len(data.index)] = {'DateTime': previous_row.DateTime+datetime.timedelta(
#             minutes=60*3*24*i/50 // points_to_predict), 'WSPD': pred_wspd}
#         data['SMA60'] = data['WSPD'].rolling(60).mean().shift(1)
#         data['SMA30'] = data['WSPD'].rolling(30).mean().shift(1)
#         data['SMA10'] = data['WSPD'].rolling(10).mean().shift(1)
#         data['SMA5'] = data['WSPD'].rolling(5).mean().shift(1)
#         data['SMA3'] = data['WSPD'].rolling(3).mean().shift(1)
#         data['SMA1'] = data['WSPD'].rolling(1).mean().shift(1)
#     for index, row in tswspd.iterrows():
#         data_list.append({'datetime': row['DateTime'], 'wspd': row['WSPD']})
#     data_dict = {'data': data_list}
#     # print(data_dict)
#     return jsonify(data_dict)
