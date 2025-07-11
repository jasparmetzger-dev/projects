import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date

def plot(data1, data2, y_label):
    plt.figure(figsize=(10, 6))

    plt.plot(data1, color= 'blue')
    plt.plot(data2, color= 'red')

    plt.title(f'Comparison in {y_label}')
    plt.xlabel('Date')
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()

def volatility(data1, data2, period):
    daily1 = data1.pct_change()
    data1 = daily1.rolling(window= period).std()

    daily2 = data2.pct_change()
    data2 = daily2.rolling(window= period).std()

    return data1, data2

def match_inp(s, data1, data2):
    match s:
        case 'standart':
            parameter = 'Price (USD)'

        case 'deviation':
            p = int(input('Chosen period (in days): '))
            data1, data2 = volatility(data1, data2, p)
            parameter = 'Deviation (%)'

        case 'annual volitility':
            p = int(input('Chosen period (in days): '))
            vol1, vol2 = volatility(data1, data2, p)
            anual = 252 ** 0.5
            data1 = vol1 * anual
            data2 = vol2 * anual
            parameter = 'Annual volatility (%)'

        case 'avg':
            avg_len = int(input('How long should the average be: '))
            data1 = data1.rolling(window= avg_len).mean()
            data2 = data2.rolling(window= avg_len).mean()
            parameter = 'Price (USD)'
    
    return data1, data2, parameter

def main():
    startday = '2020-01-01'
    endday = date.today()

    name1 = input('Ticker for the first stock: ').upper()
    name2 = input('Ticker for the second stock: ').upper()

    stock1_data = yf.download(name1, start= startday, end= endday)
    data1 = stock1_data['Close']
    stock2_data = yf.download(name2, start= startday, end= endday)
    data2 = stock2_data['Close']

    inp = input('What would you like to calculate? ').lower()

    a, b, c = match_inp(inp, data1, data2)
    plot(a, b, c)

main()