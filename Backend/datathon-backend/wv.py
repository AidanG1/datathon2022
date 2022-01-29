import pandas as pd
import math
import numpy as np

def wind_vector(df):

    #a grand team effort
    #involving Jacob Kasner
    #and Noah Spector

    radians = df["WDIR"].apply(lambda x: math.cos(180/math.pi * x))

    df["WX"] = df["WSPD"] * radians

    df["WY"] = df["WSPD"]* np.sin(180/math.pi * df["WDIR"])