from sklearn.linear_model import LinearRegression as LR
from convert_to_df import convert_txt_to_df
import financialanalysis as fa
from matplotlib import pyplot as plt

from lineartree import LinearTreeRegressor
from sklearn.datasets import make_regression

STATION = "KIKT"

start_df = convert_txt_to_df(STATION)

# start_df["datetime_str"] = start_df.apply(lambda row: row["#YY"] + row["MM"], axis=1)

print(start_df.head())

model = LR()

slope, intercept, x, fittedline = fa.timeseriesLinearRegression(
    start_df["DateTime"], start_df["WSPD"])


# Make graph of the results
fig = plt.figure(figsize=(12, 7))  # make canvas of picture
plt.plot(start_df["DateTime"], start_df["WSPD"], label="original")
plt.plot(start_df["DateTime"], fittedline, label="prediction")
plt.grid()
plt.xlabel("Date")
plt.ylabel("WindSpeed")
plt.suptitle("Timeseries of WSPD for Station " + STATION)
plt.legend(loc="best")
fig.savefig("simple_LR.png")  # save as image

x = start_df[["ATMP", "DEWP", "VIS", "GSTD", "TIME"]]
y = start_df["WX"]

regr = LinearTreeRegressor(base_estimator=model)
regr.fit(x, y)
