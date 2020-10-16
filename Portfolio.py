from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
import datetime

yf.pdr_override()

stocklist = ['AAPL', 'TSLA', 'AMZN','GOOG']

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=365)
unused = ['Open', 'High', 'Low', 'Close', 'Volume']

stocks = pd.DataFrame()

for i in range(0, len(stocklist)):
    data = pdr.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
    for word in unused:
        data = data.drop(word, 1)

    stocks = pd.concat([stocks, data], axis=1)

stocks.columns = [stocklist]

log_ret = np.log(stocks/stocks.shift(1))

np.random.seed(42)
num_ports = 1000
all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for x in range(num_ports):
    weights = np.array(np.random.random(len(stocklist)))
    weights = weights/np.sum(weights)

    all_weights[x,:] = weights

    ret_arr[x] = np.sum( (log_ret.mean() * weights * 252))

    vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))

    sharpe_arr[x] = ret_arr[x]/vol_arr[x]


max_sr_ret = ret_arr[sharpe_arr.argmax()]
max_sr_vol = vol_arr[sharpe_arr.argmax()]


def get_ret_vol_sr(weights):
    weights = np.array(weights)
    ret = np.sum(log_ret.mean()*weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
    sr = ret/vol
    return np.array([ret, vol, sr])

def neg_sharpe(weights):
    return get_ret_vol_sr(weights)[2] * -1

def check_sum(weights):
    return np.sum(weights)-1

cons = ({'type':'eq', 'fun':check_sum})
init_guess = np.full((1,len(stocklist)),1/len(stocklist))
bounds = [[0,1]]*len(stocklist)

opt_results = minimize(neg_sharpe, init_guess, method='SLSQP', bounds=bounds, constraints=cons)
print(opt_results)

print(get_ret_vol_sr(opt_results.x))

frontier_y = np.linspace(0.5,2,200)

def minimize_volatility(weights):
    return get_ret_vol_sr(weights)[1]

frontier_x = []

for possible_return in frontier_y:
    cons = ({'type':'eq', 'fun':check_sum},
            {'type':'eq', 'fun':lambda w: get_ret_vol_sr(w)[0] - possible_return})
    result = minimize(minimize_volatility, init_guess, method = 'SLSQP', bounds=bounds, constraints=cons)
    frontier_x.append(result['fun'])

plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.plot(frontier_x, frontier_y, 'r--', linewidth=3)
plt.show()
