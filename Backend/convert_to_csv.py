from gettext import gettext
import requests
import pandas as pd
import numpy as np

def get_txt(station: str):
    r = requests.get(f'https://www.ndbc.noaa.gov/data/realtime2/{station.upper()}.txt').text
    return r

def convert_txt_to_pd(station: str):
    txt = get_txt(station)
    lines = txt.split('\n')
    # for line in lines:
    #     print(line.split('\t'))
    with open('data.txt','w') as data:
        for line in lines:
            data.write(str(line.split()))
        data.close()
    return lines

print(convert_txt_to_pd('KBQX'))