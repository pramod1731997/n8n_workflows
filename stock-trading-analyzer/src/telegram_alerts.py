from telegram import Bot
import json
import logging


def __init__(self, config_path='config.json'):
        self.config = self.load_config(config_path)
        self.bot = Bot(token=self.config['telegram']['token'])
        self.chat_id = self.config['telegram']['chat_id']
        self.logger = self.setup_logger()

def load_config(self, path):
        with open(path, 'r') as f:
            return json.load(f)

def setup_logger(self):
        logger = logging.getLogger('TelegramAlerts')
        handler = logging.FileHandler('telegram_alerts.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

def send_alert(self, ticker, signal_type, confidence, current_price):
        message = (f"Ticker: {ticker}\n"
                   f"Signal: {signal_type}\n"
                   f"Confidence: {confidence:.2f}\n"
                   f"Current Price: {current_price:.2f}")
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
            self.logger.info(f"Alert sent for {ticker}: {signal_type} with confidence {confidence}")
        except Exception as e:
            self.logger.error(f"Failed to send alert for {ticker}: {e}")