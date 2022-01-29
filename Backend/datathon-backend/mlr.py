from sklearn.linear_model import LinearRegression as LR
from convert_to_df import convert_txt_to_df
import financialanalysis as fa
from matplotlib import pyplot as plt

start_df = convert_txt_to_df("KIKT")
features = start_df[["GST", "VIS"]]

# start_df["datetime_str"] = start_df.apply(lambda row: row["#YY"] + row["MM"], axis=1)

print(start_df.tail())

model = LR()

# slope, intercept, x, fittedline = fa.timeseriesLinearRegression(start_df["datetime"], start_df["relative_price_change_CTtoBS"])


# ## Make graph of the results
# fig = plt.figure(figsize=(12, 7)) # make canvas of picture. figsize is optional
# plt.plot(data["datetime"], data["relative_price_change_CTtoBS"], label="original") # draw line (label is optional)
# plt.plot(data["datetime"], fittedline, label="prediction") # add one more line (label is optional)
# plt.grid() # optional
# plt.xlabel("Date") # optional
# plt.ylabel("Price change from Jan 2020") # optional
# plt.suptitle("Example of linear regression of timeseries data") # optional
# plt.legend(loc="best") # optional
# fig.savefig("example_linear_regression.png") # save as image