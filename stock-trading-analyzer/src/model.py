from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import joblib
import logging

class StockModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = RandomForestClassifier()
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger('StockModel')
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('stock_model.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def train(self, X, y):
        self.model.fit(X, y)
        joblib.dump(self.model, self.model_path)
        self.logger.info('Model trained and saved to %s', self.model_path)

    def predict(self, X):
        return self.model.predict(X)

    def load_model(self):
        self.model = joblib.load(self.model_path)
        self.logger.info('Model loaded from %s', self.model_path)

    def backtest(self, X, y):
        predictions = self.predict(X)
        accuracy = np.mean(predictions == y)
        self.logger.info('Backtest accuracy: %.2f%%', accuracy * 100)
        return accuracy

    def update_model(self, new_data, new_labels):
        self.train(new_data, new_labels)
        self.logger.info('Model updated with new data')