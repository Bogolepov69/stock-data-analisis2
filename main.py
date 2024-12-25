import data_download as dd
import data_plotting as dplt
import pandas as pd


def main():
    """
    Основная функция для запуска программы.

    Опрашивает пользователя о тикерах и периодах,
    загружает данные, расчитывает скользящую среднюю и отображает график.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    window_size = 20

    try:
        stock_data = dd.fetch_stock_data(ticker, period)
        if stock_data is None:
            print("Загрузка данных не удалась. Проверьте подключение к интернету и корректность тикера.")
        else:
            stock_data_with_sma = dd.add_moving_average(stock_data, window_size)
            if stock_data_with_sma is not None:
                dplt.create_and_save_plot(stock_data_with_sma, ticker, period)
            else:
                print("Ошибка при расчете скользящего среднего.")

        # Вызов функции для расчета средней цены
        if stock_data is not None:
            calculate_and_display_average_price(stock_data)

    except Exception as e:
        print(f"Произошла критическая ошибка: {e}")


def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия акций.

    Args:
        data: pandas DataFrame с данными о ценах акций, содержащий столбец 'Close'.
    """
    if data is None or not isinstance(data, pd.DataFrame) or 'Close' not in data.columns:
        print("Ошибка: Некорректные входные данные. DataFrame должен содержать столбец 'Close'.")
        return

    if data['Close'].isnull().all():  # Проверяем, не содержит ли столбец только NaN значения
        print("Ошибка: Столбец 'Close' содержит только NaN значения.")
        return

    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия: {average_price:.2f}")


if __name__ == "__main__":
    main()