import pandas as pd
import math
import numpy as np


def wind_vector(df):
    # a grand team effort
    # involving Jacob Kasner
    # and Noah Spector

    radians = df["WDIR"].apply(lambda x: math.cos(180 / math.pi * x))

    df["WX"] = df["WSPD"] * radians

    df["WY"] = df["WSPD"] * np.sin(180 / math.pi * df["WDIR"])


def lstm_clean(df):
    # everything is more or less continuous except angles
    # so just interpolate them
    # angles might be tricky but just hope there isn't too much data missing
    df["WSPD"].interpolate(inplace=True);
    df["WDIR"].interpolate(inplace=True);
    df["DEWP"].interpolate(inplace=True);
    df["ATMP"].interpolate(inplace=True);
    df["PRES"].interpolate(inplace=True);

    df["VIS"].interpolate(inplace=True);

    gst = df["GST"].fillna(df["WSPD"]);
    df["GSTD"] = gst - df["WSPD"];
    df["TIME"] = np.cos((df["hour"] + df["minute"] / 60) / 24 * 2 * math.pi)

    # drop some columns
    df.dropna(axis=1, inplace=True)
    df.drop(columns=["hour", "minute", "year", "month", "day"], inplace=True)
