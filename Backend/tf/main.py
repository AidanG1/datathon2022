

import json
import requests
import numpy

def index():
    data = json.dumps({"signature_name": "serving_default", "instances": numpy.zeros((32,72,6)).tolist()})
    #print('Data: {} ... {}'.format(data[:50], data[len(data) - 52:]))
    #print(window.example[0].shape)

    headers = {"content-type": "application/json"}
    json_response = requests.post('http://8750-35-222-127-158.ngrok.io/v1/models/lstm_model:predict', data=data, headers=headers)
    #print(json_response.text)
    #print(json.loads(json_response.text)["predictions"])

    #return jsonify({'Success!': 'Yay'})

index()