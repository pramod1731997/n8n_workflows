import yfinance as yf
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_stock_data(ticker):
    try:
        logging.info(f"Fetching data for {ticker}")
        stock_data = yf.download(ticker, period='1d', interval='1m')
        if stock_data.empty:
            logging.warning(f"No data found for {ticker}")
            return None
        return stock_data
    except Exception as e:
        logging.error(f"Error fetching data for {ticker}: {e}")
        return None

def fetch_multiple_stocks(tickers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_stock_data, tickers))
    return results

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

if __name__ == "__main__":
    config = load_config('../config.json')
    tickers = config.get('stock_list', [])
    stock_data = fetch_multiple_stocks(tickers)
    # Further processing of stock_data can be done here.