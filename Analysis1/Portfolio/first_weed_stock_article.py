import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# start = datetime.datetime(2012, 1, 4)
# end = datetime.datetime(2017, 12, 13)
# '' = web.DataReader('', 'yahoo', start, end)
# ''.to_csv('')

# Fomat the columns and rows for our purposes.
ogi = pd.read_csv('OGIcomp.csv', index_col=0, parse_dates=True)
ogi = ogi.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1)
ogi = ogi.rename(columns={'Adj Close':'OGI'})
print(ogi.info())

weed = pd.read_csv('WEEDcomp.csv', index_col=0, parse_dates=True)
weed = weed.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1)
weed = weed.rename(columns={'Adj Close':'WEED'})
print(weed.info())

aph = pd.read_csv('APHcomp.csv', index_col=0, parse_dates=True)
aph = aph.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1)
aph = aph.rename(columns={'Adj Close':'APH'})
print(aph.info())

#Merge all dataframes together and print to a new csv file.
merged1 = ogi.merge(weed, how='left', left_index=True, right_index=True)
print(merged1.info())

df = merged1.merge(aph, how='left', left_index=True, right_index=True)

df.plot()
plt.show()





