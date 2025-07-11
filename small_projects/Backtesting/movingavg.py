import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

#strategy data is red, market data is blue
ticker = 'MSCI'
start = '2020-01-01'
LMA_len = 200
SMA_len = 50

#get correct data

data = yf.download(ticker, start= start, end= date.today())

data['SMA'] = data['Close'].rolling(window= SMA_len).mean()
data['LMA'] = data['Close'].rolling(window= LMA_len).mean()

#implement buy/sell

data['Action'] = 0
data.loc[data['SMA'] > data['LMA'], 'Action'] = 1 #bought
data.loc[data['SMA'] <= data['LMA'], 'Action'] = -1 #not bought

#compare

data['Position'] = data['Action'].shift(1)
data['Daily'] = data['Close'].pct_change()
data['Strategy'] = data['Position'] * data['Daily']

cumulative_strategy_return = (1 + data['Strategy']).cumprod()
cumulative_market_return = (1 + data['Daily']).cumprod()

plt.figure(figsize= (10, 6))

plt.plot(cumulative_market_return, color= 'blue')
plt.plot(cumulative_strategy_return,  color= 'red')

plt.show()