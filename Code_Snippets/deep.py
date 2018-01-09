import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# from keras.layers import Dense, Activation
# from keras.models import Sequential

# start = datetime(1978, 1, 13)
# end = datetime(2017, 10, 6)
# # Set the ticker
# ticker = 'IBM'
# # Set the data source
# data_source = 'yahoo'
# # Import the stock prices, save them and read them again locally
# stock_prices = web.DataReader(ticker, data_source, start, end)
# stock_prices.to_csv('deep.csv')
ibm = pd.read_csv('deep.csv', index_col=0, parse_dates=True, na_values='0')

ibm['Log_Ret'] = np.log(ibm['Close'] / ibm['Close'].shift(1)).fillna(0)
ibm['Volatility'] = pd.rolling_std(ibm['Log_Ret'], window=252).fillna(0) * np.sqrt(252)
ibm['Open_Dev'] = np.std(ibm['Open'])
ibm['High_Dev'] = np.std(ibm['High'])
ibm['Low_Dev'] = np.std(ibm['Low'])

ibm = np.array(ibm)
x_test, x_train, y_test, y_train = train_test_split(ibm, ibm, test_size=0.3, stratify=y)


model = Sequential()
model.add(Dense(100, activation='relu', input_shape=None))
model.add(Dense(100, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit()

score = model.evaluate(x_test, y_test, batch_size=)

