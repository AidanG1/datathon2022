import requests
import pandas as pd
import numpy as np
from wv import wind_vector

def get_txt(station: str):
    r = requests.get(f'https://www.ndbc.noaa.gov/data/realtime2/{station.upper()}.txt').text
    return r

def clean_data(element):
    if element == "MM":
        return np.NaN
    
    return float(element)

def convert_txt_to_df(station: str):
    txt = get_txt(station)
    lines = txt.split('\n')
    second_split_lines = []
    for line in lines:
        second_split_lines.append(line.split())
    df = pd.DataFrame(second_split_lines)
    df = df.rename(columns=df.iloc[0])
    df = df.drop([len(df)-1, 1, 0])

    new_df = df.applymap(clean_data)

    for col in ["#YY", "MM", "DD", "hh", "mm"]:
        new_df[col] = df[col].apply(int)

    wind_vector(new_df)
    return new_df

def pd_to_csv(station: str):
    convert_txt_to_df(station).to_csv(f'{station}.csv')

pd_to_csv('kbqx')