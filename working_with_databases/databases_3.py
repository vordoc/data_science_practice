import yfinance as yf

"""
Мы создали в БД sampledb новую таблицу stocks используя команды:
 mysql> USE sampledb
 mysql> CREATE TABLE stocks (ticker VARCHAR(10), date VARCHAR(10), price DECIMAL(15,2));
 
Далее получим биржевые данные с помощью библиотеки yfinance, и сохраним их в таблице stocks. 
"""

# определяем пустой список data, который будет заполнен биржевыми данными
data = []
# затем определяем список тикеров, по которым хотим извлечь данные
tickers = ['TSLA', 'FB', 'ORCL', 'AMZN']

"""В цикле передаем каждый тикер из списка tickers в функцию yfinance Ticker(). Функция возвращает объект Ticker. 
Его метод history() предоставляет данные, связанные с соответствующим тикером. В этом примере мы получаем данные 
об акциях для каждого тикера за пять последних рабочих дней (period='5d'). Метод history() возвращает данные о 
котировках в виде pandas DataFrame со столбцом Date в качестве индекса. Наконец, преобразуем этот датафрейм
в список кортежей для вставки в базу данных. Поскольку в датасет нам нужно включить столбец Date, удаляем его из 
индекса с помощью метода DataFrame reset_index(), тем самым превращая Date в обычный столбец"""

for ticker in tickers:
	tkr = yf.Ticker(ticker)
	hist = tkr.history(period='5d').reset_index()
	records = hist[['Date', 'Close']].to_records(index=False)

records = list(records)
records = [(ticker, str(elem[0])[:10], round(elem[1], 2)) for elem in records]
data = data + records
