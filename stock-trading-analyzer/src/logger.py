import logging
import os

def setup_logger(log_file='trading_analyzer.log'):
    """Sets up the logger for the application."""
    log_path = os.path.join(os.getcwd(), log_file)
    
    logging.basicConfig(
        filename=log_path,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logging.getLogger().addHandler(console_handler)

setup_logger()