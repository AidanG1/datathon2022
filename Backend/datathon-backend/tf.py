

import json
import requests
import numpy
import convert_to_df

def get_data(station: str):
    input_frame = convert_to_df.convert_txt_to_df(station)
    data = json.dumps({"signature_name": "serving_default", "instances": input_frame.tolist()})
    #print('Data: {} ... {}'.format(data[:50], data[len(data) - 52:]))
    #print(window.example[0].shape)

    headers = {"content-type": "application/json"}
    json_response = requests.post('http://8750-35-222-127-158.ngrok.io/v1/models/lstm_model:predict', data=data, headers=headers)
    #print(json_response.text)
    thing = json.loads(json_response.text)["predictions"]


    #trained for fmoa1
    wmean = 7.794434
    wstd = 3.461577
    return [thing[0][i][0] * wstd + wmean for i in range(72)]
    #return jsonify({'Success!': 'Yay'})

#print(get_data(numpy.zeros((1,72,6))))