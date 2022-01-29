

import json
import requests
import numpy
import convert_to_df

def get_data(station: str):
    input_frame = convert_to_df.convert_txt_to_df(station)
    if not all(ind in input_frame.columns for ind in ["WDIR", "WSPD", "ATMP", "GSTD", "TIME"]):
        return None
    input_frame = input_frame[["WDIR", "WSPD", "ATMP", "GSTD", "TIME"]][:72]
    print(input_frame)


    data = json.dumps({"signature_name": "serving_default", "instances": [input_frame.to_numpy().tolist()]})
    #print('Data: {} ... {}'.format(data[:50], data[len(data) - 52:]))
    #print(window.example[0].shape)

    headers = {"content-type": "application/json"}
    json_response = requests.post('http://2dad-35-237-44-38.ngrok.io/v1/models/lstm_model:predict', data=data, headers=headers)
    parsed = json.loads(json_response.text)
    if not "predictions" in parsed:
        return None
    thing = parsed["predictions"]


    #trained for fmoa1
    wmean = 7.745359
    wstd = 4.151231
    return [thing[0][i][0] * wstd + wmean for i in range(72)]
    #return jsonify({'Success!': 'Yay'})

#print(get_data("pcnt2"))