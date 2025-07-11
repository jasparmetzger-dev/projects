import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Parameters
stock = "AAPL"
start_date = "2018-01-01"
end_date = "2023-01-01"
rolling_window = 20
z_entry_threshold = 2.0  # Threshold for entering a position
capital = 10000  # Initial capital

# Fetch stock data
data = yf.download(stock, start=start_date, end=end_date)
data['Price'] = data['Close']

# Calculate rolling mean and standard deviation
data['Rolling Mean'] = data['Price'].rolling(window=rolling_window).mean()
data['Rolling Std'] = data['Price'].rolling(window=rolling_window).std()

# Calculate Z-score
data['Z-Score'] = (data['Price'] - data['Rolling Mean']) / data['Rolling Std']

# Define trading signals
data['Signal'] = 0  # No position
data.loc[data['Z-Score'] > z_entry_threshold, 'Signal'] = -1  # Sell signal
data.loc[data['Z-Score'] < -z_entry_threshold, 'Signal'] = 1  # Buy signal

# Carry forward signals
data['Position'] = data['Signal'].replace(to_replace=0, method='ffill')

# Backtest logic
data['Daily Return'] = data['Price'].pct_change()
data['Strategy Return'] = data['Position'].shift(1) * data['Daily Return']

# Calculate cumulative returns
data['Portfolio Value'] = (1 + data['Strategy Return']).cumprod() * capital
data['Buy and Hold Value'] = (1 + data['Daily Return']).cumprod() * capital

# Visualization
plt.figure(figsize=(14, 7))

# Stock price and signals
plt.subplot(2, 1, 1)
plt.plot(data.index, data['Price'], label='Price')
plt.plot(data.index, data['Rolling Mean'], label='Rolling Mean')
plt.scatter(data.index[data['Signal'] == 1], data['Price'][data['Signal'] == 1], label='Buy Signal', marker='^', color='green')
plt.scatter(data.index[data['Signal'] == -1], data['Price'][data['Signal'] == -1], label='Sell Signal', marker='v', color='red')
plt.legend()
plt.title(f'{stock} Price with Buy/Sell Signals')

# Portfolio value
plt.subplot(2, 1, 2)
plt.plot(data.index, data['Portfolio Value'], label='Strategy Portfolio Value', color='blue')
plt.plot(data.index, data['Buy and Hold Value'], label='Buy and Hold Value', color='orange')
plt.legend()
plt.title('Portfolio Performance')

plt.tight_layout()
plt.show()

# Performance metrics
total_return_strategy = data['Portfolio Value'].iloc[-1] / capital - 1
total_return_bh = data['Buy and Hold Value'].iloc[-1] / capital - 1
sharpe_ratio = data['Strategy Return'].mean() / data['Strategy Return'].std() * np.sqrt(252)

print(f"Strategy Total Return: {total_return_strategy:.2%}")
print(f"Buy and Hold Total Return: {total_return_bh:.2%}")
print(f"Strategy Sharpe Ratio: {sharpe_ratio:.2f}")
