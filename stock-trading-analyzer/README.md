# Stock Trading Analyzer

## Overview
The Stock Trading Analyzer is a Python application designed to fetch live stock data from NSE/BSE, perform technical analysis, and provide buy/sell predictions using machine learning. It integrates with the Telegram API to send alerts based on trading signals and is configurable via a `config.json` file.

## Features
- Continuous fetching of live stock data using `yfinance`.
- Parallel processing for efficient data fetching and analysis.
- Technical indicator analysis including EMA, RSI, MACD, Bollinger Bands, and ADX.
- Machine learning model training for buy/sell predictions.
- Telegram alerts for trading signals.
- Robust logging capabilities.

## Project Structure
```
stock-trading-analyzer
├── src
│   ├── main.py               # Entry point of the application
│   ├── config.py             # Configuration management
│   ├── data_fetcher.py       # Live stock data fetching
│   ├── indicators.py          # Technical indicators calculations
│   ├── model.py               # Machine learning model training
│   ├── telegram_alerts.py     # Telegram API integration for alerts
│   ├── utils.py               # Utility functions
│   └── logger.py              # Logging setup
├── config.json                # Configuration settings
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-trading-analyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the `config.json` file with your stock list, thresholds, and Telegram API credentials.

## Usage
To start the application, run the following command:
```
python src/main.py
```

The application will continuously fetch stock data, perform analysis, and send alerts based on the configured settings.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.