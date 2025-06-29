import json

class Config:
    def __init__(self, config_file='/workspaces/n8n_workflows/stock-trading-analyzer/config.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get_stock_list(self):
        return self.settings.get('stocks', [])

    def get_thresholds(self):
        return self.settings.get('thresholds', {})

    def get_telegram_credentials(self):
        return {
            'chat_id': self.settings.get('telegram', {}).get('chat_id'),
            'token': self.settings.get('telegram', {}).get('token')
        }

    def get_ml_model_path(self):
        return self.settings.get('ml_model_path', '')