# from sklearn.model_selection import train_test_split
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import convert_to_df
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score

# from convert_to_df import convert_txt_to_df

# input_df = convert_txt_to_df("KIKT")

# TARGET = "WDIR"

# def mlr2(df: pd.DataFrame):
#     df['SMA60'] = df[TARGET].rolling(60).mean().shift(1)
#     df['SMA30'] = df[TARGET].rolling(30).mean().shift(1)
#     df['SMA10'] = df[TARGET].rolling(10).mean().shift(1)
#     df['SMA5'] = df[TARGET].rolling(5).mean().shift(1)
#     df['SMA3'] = df[TARGET].rolling(3).mean().shift(1)
#     df['SMA1'] = df[TARGET].rolling(1).mean().shift(1)
#     df = df.dropna()

#     # x = df[['ATMP', 'VIS', 'SMA60', 'SMA30', 'SMA10','SMA4','GSTD','TIME']].dropna()
#     # x = df[['ATMP', 'VIS', 'SMA60', 'SMA30', 'SMA10','SMA3','SMA1','GSTD','TIME']].dropna()
#     x = df[['SMA60', 'SMA30', 'SMA10']].dropna()
#     # x = df[['SMA1']].dropna()
#     y = df[TARGET].dropna()

#     x_train, x_test, y_train, y_test = train_test_split(
#         x, y, test_size=0.3, random_state=100)
#     mlr = LinearRegression()
#     mlr.fit(x_train, y_train)
#     y_pred_mlr = mlr.predict(x_test)
    
#     return mlr.coef_
#     # return mlr

#     plt.scatter(y_test, y_pred_mlr, c='green')
#     x = np.linspace(0,25,200)
#     y = x
#     plt.plot(x, y)
#     plt.show()
#     print(r2_score(y_test, y_pred_mlr))


# print(mlr2(input_df))