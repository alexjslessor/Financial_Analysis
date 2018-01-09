import pandas_datareader.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.core import datetools
import numpy as np
#aapl = quandl.get("WIKI/IBM", start_date="2006-10-01", end_date="2017-01-01")

all_data = pd.read_csv('big4.csv', parse_dates=True, index_col=0)

all_adj_close = all_data[['Adj Close']]

# Calculate the returns
all_returns = np.log(all_adj_close / all_adj_close.shift(1))

# Isolate the AAPL returns
aapl_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'AAPL']
aapl_returns.index = aapl_returns.index.droplevel('Ticker')

# Isolate the MSFT returns
msft_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'MSFT']
msft_returns.index = msft_returns.index.droplevel('Ticker')

# Build up a new DataFrame with AAPL and MSFT returns
return_data = pd.concat([aapl_returns, msft_returns], axis=1)[1:]
return_data.columns = ['AAPL', 'MSFT']

# Add a constant
X = sm.add_constant(return_data['AAPL'])

# Construct the model
model = sm.OLS(return_data['MSFT'],X).fit()

# Print the summary
print(model.summary())
