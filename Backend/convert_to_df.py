import requests
import pandas as pd
import numpy as np

def get_txt(station: str):
    r = requests.get(f'https://www.ndbc.noaa.gov/data/realtime2/{station.upper()}.txt').text
    return r

def convert_txt_to_df(station: str):
    txt = get_txt(station)
    lines = txt.split('\n')
    second_split_lines = []
    for line in lines:
        second_split_lines.append(line.split())
    return pd.DataFrame(second_split_lines)

# print(convert_txt_to_df('KBQX'))