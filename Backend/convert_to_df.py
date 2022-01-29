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
    df = pd.DataFrame(second_split_lines)
    df = df.rename(columns=df.iloc[0])
    df = df.drop([len(df)-1,1, 0])
    return df

def pd_to_csv(station: str):
    convert_txt_to_df(station).to_csv(f'{station}.csv')

pd_to_csv('kbqx')