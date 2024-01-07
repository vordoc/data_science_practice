import pandas as pd
import yfinance as yf
import json

"""Мы разобрали, как создать pandas DataFrame путем объединения нескольких 
объектов Series. 
Также создать DataFrame можно, загрузив данные из базы данных, файла CSV, запроса working_with_files_and_API 
или из другого внешнего источника с помощью одного из методов для чтения из библиотеки pandas. 
Эти методы позволяют читать различные типы данных, такие как JSON и Excel, и преобразовывать их 
в датафреймы"""



"""Возьмем уже готовый датафрейм используя библиотеку yahoo finance"""
# возьмем тикер бумаги Тесла
tkr = yf.Ticker('TSLA')
# берем данные о бумаге за пятидневный период
hist = tkr.history(period="5d")
print(hist)
# уберем столбцы с нулевыми значениями
hist = hist.drop("Dividends", axis=1)
hist = hist.drop("Stock Splits", axis=1)
# сбросим индексы
hist = hist.reset_index()
# переиндексируем датафрейм, указав столбец Date в качестве индекса
hist = hist.set_index('Date')
print(hist)
print("\n----------------------------------------------------------\n")




"""Преобразуем документ JSON в объект pandas. 
Используемый в примере датасет содержит данные о месячной заработной плате трех 
сотрудников. Каждому сотруднику присвоен уникальный идентификатор (ID) в столбце Empno"""
data = [
	{"Empno": 9001, "Salary": 3000},
	{"Empno": 9002, "Salary": 2800},
	{"Empno": 9003, "Salary": 2500}
]

# создадим файл json и запишем в него данные из списка data
with open("data_1.json", "w") as json_1:
	json.dump(data, json_1)

# относительный путь до файла json
path_to_json = './data_1.json'

"""C помощью метода read_json преобразуем файл json в датафрейм 
(в метод передаётся либо объект path - путь до нужного JSON-файла, либо URL HTTP working_with_files_and_API, 
который публикует данные в формате JSON)"""
salary = pd.read_json(path_to_json)
# выбираем столбец Empno в качестве индекса датафрейма
salary = salary.set_index('Empno')
print(salary)
print("\n----------------------------------------------------------\n")





"""Ещё одна распространенная практика — создание pandas DataFrame из стандартных структур данных Python. 
Например, можно создать датафрейм из списка списков"""
data = [['9001', 'Jeff Russell', 'sales'],
		['9002', 'Jane Boorman', 'sales'],
		['9003', 'Tom Heints', 'sales']]

"""явно создаем датафрейм, определяя названия столбцов"""
emps = pd.DataFrame(data, columns=['Empno', 'Name', 'Job'])

"""используем словарь column_types, чтобы изменить типы данных, установленные для столбцов по умолчанию
Этот шаг необязателен, но он может иметь решающее значение при объединении одного датафрейма с другим, 
поскольку сделать это можно только со столбцами, содержащими данные одного типа."""
column_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(column_types)

"""в качестве индекса устанавливаем столбец Empno"""
emps = emps.set_index('Empno')

print(emps)



