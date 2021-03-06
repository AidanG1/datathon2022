import requests
import pandas as pd
import numpy as np
from wv import wind_vector, lstm_clean


def get_txt(station: str):
    r = requests.get(
        f'https://www.ndbc.noaa.gov/data/realtime2/{station.upper()}.txt').text
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
    num = 4000
    if len(df) < num:
        num = len(df)
    df = df[:num]
    df = df.rename(columns=df.iloc[0])
    df = df.drop([len(df)-1, 1, 0])

    new_df = df.applymap(clean_data)

    for col in ["#YY", "MM", "DD", "hh", "mm"]:
        new_df[col] = df[col].apply(int)

    new_df = new_df.rename(columns={'#YY': "year", 'MM': 'month', "DD":"day", "hh":"hour", "mm":"minute"})
    df_datetime = new_df[['year', 'month', 'day', 'hour', 'minute']]
    df_datetime = pd.to_datetime(df_datetime)
    new_df.insert(0, 'DateTime', df_datetime, allow_duplicates=True)

    lstm_clean(new_df)
    wind_vector(new_df)
    return new_df.iloc[::-1]


def pd_to_csv(station: str):
    convert_txt_to_df(station).to_csv(f'{station}.csv')

# print(convert_txt_to_df('kbqx'))
# stations = "kmis poro3 pegf1 aamc1 pxoc1 vtbt2".split(" ")
# for s in stations:
#     pd_to_csv(s)
