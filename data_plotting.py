import matplotlib.pyplot as plt
import pandas as pd

def create_and_save_plot(data, ticker, period, filename=None):
    """
    Создает и сохраняет график цен акций и скользящих средних.

    Args:
        data (pandas.DataFrame): DataFrame с данными о ценах акций и скользящими средними.
        ticker (str): Тикер акции.
        period (str): Временной период для данных.
        filename (str, optional): Имя файла для сохранения графика. Defaults to None.
    """
    if data is None or data.empty:
        print("Ошибка: Данные отсутствуют. Невозможно построить график.")
        return

    try:
        # Определяем ось X автоматически, используя индекс или столбец 'Date', если он есть
        if pd.api.types.is_datetime64_any_dtype(data.index):
            x_axis = data.index.to_numpy()
        elif 'Date' in data.columns and pd.api.types.is_datetime64_any_dtype(pd.to_datetime(data['Date'], errors='coerce')):
            x_axis = pd.to_datetime(data['Date'], errors='coerce').to_numpy()
        else:
            print("Ошибка: Невозможно определить ось X (дата). Проверьте данные.")
            return

        plt.figure(figsize=(10, 6))
        plt.plot(x_axis, data['Close'].values, label='Close Price')
        plt.plot(x_axis, data['Moving_Average'].values, label='Moving Average')

        plt.title(f"{ticker} Цена акций с течением времени")
        plt.xlabel("Дата")
        plt.ylabel("Цена")
        plt.legend()

        if filename is None:
            filename = f"{ticker}_{period}_stock_price_chart.png"
        plt.savefig(filename)
        print(f"График сохранен как {filename}")

    except Exception as e:
        print(f"Ошибка при построении графика: {e}")