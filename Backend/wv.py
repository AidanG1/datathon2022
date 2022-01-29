import pandas as pd
import math

def wind_vector(df):
    df["WX"] = df["WSPD"]* math.cos(180/math.pi * df["WDIR"])
    df["WY"] = df["WSPD"]* math.sin(180/math.pi * df["WDIR"])