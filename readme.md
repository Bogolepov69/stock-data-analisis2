# Анализ и визуализация данных об акциях

Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. Он использует библиотеку `yfinance` для получения данных и `matplotlib` для создания графиков. Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.

## Структура проекта

Проект состоит из трех основных модулей:

1.  `data_download.py`:  Отвечает за загрузку данных об акциях.
2.  `data_plotting.py`:  Отвечает за визуализацию данных.
3.  `main.py`:  Основной скрипт для запуска программы.

## Зависимости

•   `yfinance`
•   `matplotlib`
•   `pandas`
•   `requests`

## Установка

1.  Клонируйте репозиторий: 
2. bash
  git clone [https://github.com/Bogolepov69/stock-data-analisis2]
3. Перейдите в директорию проекта:
4. Создайте и активируйте виртуальное окружение:
5. bash
  python -m venv venv
  # Windows
  .\venv\Scripts\activate
  # macOS/Linux
  source venv/bin/activate
1. Установите необходимые пакеты:
2. bash
  pip install -r requirements.txt

## Использование

1. Запустите main.py: bash
    python main.py
2. Следуйте инструкциям в консоли для ввода тикера акции и временного периода.

3. Программа загрузит данные, рассчитает скользящее среднее и построит график.

▌Примеры работы

```markdown
    ### Пример 1: Загрузка данных Apple (AAPL) за 1 месяц
    Пользователь вводит AAPL как тикер и 1mo как период. Программа загружает исторические данные за 1 месяц и строит график
![Скриншот загрузки данных Apple](images/aapl_1mo_screenshot.png)
```
```markdown
    ### Пример 2: Загрузка данных Google (GOOGL) за 1 год
Пользователь вводит GOOGL как тикер и 1y как период. Программа загружает исторические данные за 1 год и строит график.
![Скриншот загрузки данных Google](images/googl_1y_screenshot.png)
```

```markdown
    ###Пример 3: Обработка отсутствия данных
Если данные для введенного тикера или периода не найдены (например, если пользователь вводит некорректный тикер), программа выведет соответствующее сообщение об ошибке и не вызовет исключения.
![Скриншот сообщения об ошибке](images/error message_screenshot.png)
```
```markdown
    ###Пример 4: Вычисление средней цены

Функция calculate_and_display_average_price вычисляет и отображает среднюю цену закрытия акций за выбранный период.
![Скриншот показывает среднюю цену закрытия акций за выбранный период](images/calculate_and_display_average_price_screenshot.png)
```

python
import pandas as pd
from data_download import fetch_stock_data
from main import calculate_and_display_average_price

# Получаем данные об акциях Apple за 1 месяц
data = fetch_stock_data("AAPL", "1mo")

if data is not None and not data.empty:
  # Рассчитываем и выводим среднюю цену закрытия
  calculate_and_display_average_price(data)
else:
  print("Невозможно вычислить среднюю цену закрытия из-за отсутствия данных.")


▌ Подробнее про функции
 •  data_download.py:
    *  fetch_stock_data(ticker, period): Загружает исторические данные об акциях.
    *  add_moving_average(data, window_size): Добавляет столбец со скользящим средним.

  •  data_plotting.py:
    *  create_and_save_plot(data, ticker, period, filename=None): Создает и сохраняет график.
  •  main.py:
    *  main(): Основная функция для запуска программы.
    *  calculate_and_display_average_price(data): Функция для расчета и отображения средней цены закрытия.



