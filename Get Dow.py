import requests, bs4
import datetime
import pandas_datareader as web
import pandas as pd
import time
import matplotlib.pyplot as plt
from matplotlib import style
import os.path

def get_tickers(url):
    nasd = requests.get(url)
    nasdaqsoup = bs4.BeautifulSoup(nasd.text,"html.parser")

    nasd_products = (nasdaqsoup.findAll(class_="first text"))

    nasdaq_tickers = []
    for product in nasd_products:
        nasdaq_tickers.append(product.string)

    return (nasdaq_tickers)

(get_tickers("https://www.cnbc.com/nasdaq-100/"))

def get_stock_data(tickers):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    for ticker in tickers:
        if os.path.exists((r"C:\Users\Kaobe\PycharmProjects\Financee\venv\{}.csv").format(ticker)) == False and ticker != "Symbol":
            df = web.DataReader(ticker, 'morningstar', start, end)
            ticker = ticker.strip('')
            df.to_csv(("{}.csv").format(ticker))
        else:
            continue

    return tickers

get_stock_data(get_tickers("https://www.cnbc.com/nasdaq-100/"))

def read_data(ticker):
    print (pd.read_csv("{}.csv".format(ticker)))
    return

print (read_data("AAPL"))