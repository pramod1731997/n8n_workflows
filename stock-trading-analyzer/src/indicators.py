def calculate_ema(prices, period):
    return prices.ewm(span=period, adjust=False).mean()

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
    short_ema = calculate_ema(prices, short_window)
    long_ema = calculate_ema(prices, long_window)
    macd = short_ema - long_ema
    signal_line = calculate_ema(macd, signal_window)
    return macd, signal_line

def calculate_bollinger_bands(prices, window=20, num_std_dev=2):
    rolling_mean = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)
    return upper_band, lower_band

def calculate_adx(prices, period=14):
    high = prices['High']
    low = prices['Low']
    close = prices['Close']
    
    # Calculate True Range
    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())
    true_range = tr1.combine(tr2, max).combine(tr3, max)

    # Calculate +DI and -DI
    plus_dm = high.diff().where(lambda x: x > 0, 0)
    minus_dm = low.diff().where(lambda x: x < 0, 0).abs()
    
    plus_di = 100 * (plus_dm.rolling(window=period).mean() / true_range.rolling(window=period).mean())
    minus_di = 100 * (minus_dm.rolling(window=period).mean() / true_range.rolling(window=period).mean())
    
    # Calculate ADX
    adx = (abs(plus_di - minus_di) / (plus_di + minus_di)).rolling(window=period).mean() * 100
    return adx

def custom_breakout_strategy(prices, breakout_level):
    signals = []
    for price in prices:
        if price > breakout_level:
            signals.append(1)  # Buy signal
        else:
            signals.append(0)  # No action
    return signals

def calculate_indicators(prices, breakout_level=None):
        indicators = {}

        # EMA
        indicators['ema_12'] = calculate_ema(prices['Close'], 12)
        indicators['ema_26'] = calculate_ema(prices['Close'], 26)

        # RSI
        indicators['rsi_14'] = calculate_rsi(prices['Close'], 14)

        # MACD
        macd, signal = calculate_macd(prices['Close'])
        indicators['macd'] = macd
        indicators['macd_signal'] = signal

        # Bollinger Bands
        upper_band, lower_band = calculate_bollinger_bands(prices['Close'])
        indicators['bollinger_upper'] = upper_band
        indicators['bollinger_lower'] = lower_band

        # ADX
        indicators['adx_14'] = calculate_adx(prices, 14)

        # Custom Breakout Strategy
        if breakout_level is not None:
            indicators['breakout_signals'] = custom_breakout_strategy(prices['Close'], breakout_level)

        return indicators