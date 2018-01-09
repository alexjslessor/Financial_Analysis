import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import dask.dataframe as dd
# import quandl
import pandas_datareader.data as web
import datetime
# import statsmodels.api as sm
# import math
# import plotly as py
# from plotly import tools
# import plotly.graph_objs as go
# from bokeh.layouts import gridplot
# from bokeh.plotting import figure
# from bokeh.io import output_file, show
# from ib.ext.Contract import Contract
# from ib.ext.EWrapper import EWrapper
# from ib.ext.EClientSocket import EClientSocket
# from ib.ext.ExecutionFilter import ExecutionFilter
#Import Data
# Set start and end dates
# start = date(2000, 1, 1)
# end = date(2017, 8, 31)
end_ =datetime.datetime.now()
start_ =end_- datetime.timedelta(days=365)
# Set the ticker
ticker = 'CMED','INSY','PRMCF','MJN','GWPH','SMG','CBIS','MCOA','LXRP','GOHE','TITXF','IMLFF','PMCB','MJNA','HMMJ','IMH','IAN','THC','EMH','EMC','APH','OGI'\
			'FIRE','ACB','LEAF','WEED',
# Set the data source
data_source = 'google'
# Import the stock prices, save them and read them again locally
stock_prices = web.DataReader(ticker, data_source, start_, end_)
stock_prices.to_csv('TSLA.csv')
stock_prices = pd.read_csv('TSLA.csv', parse_dates=True, na_values='n/a', index_col=0)
#Parse Data
stock_prices['Log_Ret'] = np.log(stock_prices['Close'] / stock_prices['Close'].shift(1))
stock_prices['Volatility'] = pd.rolling_std(stock_prices['Log_Ret'], window=252) * np.sqrt(252)
#Plot Data
stock_prices[['Close', 'Volatility']].plot(subplots=True, color='red', figsize=(8, 6))

# Display and inspect the result
print(stock_prices.head(), stock_prices.info())
plt.show()
