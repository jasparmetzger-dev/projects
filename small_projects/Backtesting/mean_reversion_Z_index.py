import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'DOW'
start = '2020-01-01'
end = '2024-01-01'
rolling_len = 20
Z_entry_value = 3 #std: 2.0

data = yf.download(ticker, start= start, end= end)
data['Price'] = data['Close']

data['STD'] = data['Price'].rolling(window= rolling_len).std()
data['Mean'] = data['Price'].rolling(window= rolling_len).mean()

data['Z-Score'] = (data['Price'] - data['Mean']) / data['STD']

data['Signal'] = 0
data.loc[data['Z-Score'] > Z_entry_value, 'Signal'] = -1
data.loc[data['Z-Score'] < -1 * Z_entry_value,'Signal'] = 1
data['Position'] = data['Signal'].replace(to_replace= 0, method= 'ffill')

data['Daily'] = data['Price'].pct_change()
data['Strategy'] = (1 + (data['Position'].shift(1) * data['Daily'])).cumprod()
data['Market'] = (1 + data['Daily']).cumprod()


plt.figure(figsize=(14, 7))

# Stock price and signals
plt.subplot(2, 1, 1)
plt.plot(data.index, data['Price'], label='Price')
plt.plot(data.index, data['Mean'], label='Rolling Mean')
#show buy/sell signals
plt.scatter(data.index[data['Signal'] == 1], data['Price'][data['Signal'] == 1], label='Buy Signal', marker='^', color='green')
plt.scatter(data.index[data['Signal'] == -1], data['Price'][data['Signal'] == -1], label='Sell Signal', marker='v', color='red')
plt.legend()
plt.title(f'{ticker} Price with Buy/Sell Signals')

# Portfolio value
plt.subplot(2, 1, 2)
plt.plot(data.index, data['Strategy'], label='Strategy Portfolio Value', color='blue')
plt.plot(data.index, data['Market'], label='Buy and Hold Value', color='orange')
plt.legend()
plt.title('Portfolio Performance')

plt.tight_layout()
plt.show()