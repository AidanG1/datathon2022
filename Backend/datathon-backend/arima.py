import pmdarima as pm
from pmdarima.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import convert_to_df

# Load/split your data
df = convert_to_df.convert_txt_to_df('KBQX')
df = df.set_index('DateTime')
y = df['WSPD']
test_size = 100
train_size = len(y) - test_size
train, test = train_test_split(y, train_size=train_size)

# Fit your model
model = pm.auto_arima(train, seasonal=True, m=12)

# make your forecasts
forecasts = model.predict(test_size)

# Visualize the forecasts (blue=train, green=forecasts)
x = np.arange(y.shape[0])
plt.plot(x[:train_size], train, c='blue')
plt.plot(x[train_size:], forecasts, c='green')
plt.show()