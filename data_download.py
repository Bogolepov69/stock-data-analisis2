import yfinance as yf

def fetch_stock_data(ticker, period='1mo'):
    """
    Загружает исторические данные об акциях.

    Args:
        ticker (str): Тикер акции (например, 'AAPL').
        period (str, optional): Временной период для данных (например, '1mo', '1y'). Defaults to '1mo'.

    Returns:
        pandas.DataFrame: DataFrame с историческими данными об акциях или None в случае ошибки.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if data.empty:
            print(f"Предупреждение: Данные для тикера {ticker} за период {period} не найдены.")
            return None
        return data
    except yf.exceptions.YFinanceError as e:
        print(f"Ошибка yfinance: {e}")
        return None
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")
        return None


def add_moving_average(data, window_size=5):
    """
    Добавляет столбец с простым скользящим средним (SMA) в DataFrame.

    Args:
        data (pandas.DataFrame): DataFrame с данными о ценах акций, должен иметь столбец 'Close'.
        window_size (int, optional): Размер окна для скользящего среднего. Defaults to 5.

    Returns:
        pandas.DataFrame: DataFrame с добавленным столбцом 'Moving_Average' или None в случае ошибки.
    """
    if data is None or data.empty:
        print("Ошибка: Невозможно рассчитать скользящее среднее для пустых данных.")
        return None
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data