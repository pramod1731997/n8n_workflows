# filepath: /stock-trading-analyzer/stock-trading-analyzer/src/main.py

import json
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from data_fetcher import fetch_stock_data
from indicators import calculate_indicators
from model import StockModel
from telegram_alerts import send_alert
from config import Config
from logger import setup_logger

def main():
    # Load configuration
    config = Config()
    
    # Setup logging
    setup_logger()
    
    # Initialize scheduler
    scheduler = BackgroundScheduler()
    
    # Schedule data fetching and analysis
    scheduler.add_job(fetch_stock_data, 'interval', minutes=config.settings['fetch_interval'], args=[config])
    scheduler.add_job(calculate_indicators, 'interval', minutes=config.settings['analysis_interval'], args=[config])
    scheduler.add_job(StockModel, 'interval', days=config.settings['model_training_interval'], args=[config])
    scheduler.add_job(send_alert, 'interval', minutes=config.settings['alert_interval'], args=[config])
    
    # Start the scheduler
    scheduler.start()
    
    logging.info("Stock Trading Analyzer started.")
    
    try:
        # Keep the program running
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logging.info("Stock Trading Analyzer stopped.")

if __name__ == "__main__":
    main()