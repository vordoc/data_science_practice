import pandas as pd

"""Объединение «один-ко-многим»
При объединении методом «один-ко-многим» (one-to-many) строка из одного датафрейма 
может соответствовать сразу нескольким строкам из другого 
датафрейма. 
Рассмотрим ситуацию, когда каждый продавец из датафрейма 
emps обработал несколько заказов. 
Это можно отобразить в датафрейме orders"""

data_orders = [[2608, 9001, 35],
				[2617, 9001, 35],
				[2620, 9001, 139],
				[2621, 9002, 95],
				[2626, 9002, 218]]

"""явно создаем датафрейм orders_df, определяя названия столбцов"""
orders_df = pd.DataFrame(data_orders, columns=['Pono', 'Empno', 'Total'])
print(orders_df)


print("\n----------------------------------------------------------\n")


data_emps = [['9001', 'Jeff Russell', 'sales'],
		['9002', 'Jane Boorman', 'sales'],
		['9003', 'Tom Heints', 'sales']]

"""явно создаем датафрейм emps_df, определяя названия столбцов"""
emps_df = pd.DataFrame(data_emps, columns=['Empno', 'Name', 'Job'])

"""Приведем данные в столбце Empno к типу int (вместо str) - (в orders_df тип данных тоже int), 
иначе при слиянии датафреймов с разными типами данных в столбцах, 
по которым производится объединение мы получим ошибку 'Value error' """
emps_df['Empno'] = emps_df['Empno'].astype(int)
print(emps_df)


print("\n----------------------------------------------------------\n")

"""Теперь, когда у вас есть датафрейм orders с заказами, можно объединить его 
с датафреймом сотрудников emps_df. Это объединение типа «один ко-многим», 
поскольку один сотрудник из датафрейма emps может быть связан 
с несколькими строками из датафрейма orders.

Мы применяем метод merge() для объединения данных из 
датафреймов emps_df и orders_df, имеющих связь «один-ко-многим». 
Метод merge() позволяет указать столбцы, по которым необходимо проводить объединение, 
сразу из обоих датафреймов, используя left_on для указания столбца из вызывающего датафрейма 
и right_on — для столбца из другого датафрейма.

В этом примере мы применяем внутренний тип объединения (inner), чтобы 
включить только связанные строки из обоих датафреймов. """

emps_orders_df = emps_df.merge(orders_df, how='inner', left_on='Empno', right_on='Empno').set_index('Pono')
print(emps_orders_df)

"""Помимо отношений «один-ко-многим» и «один-к-одному», существует связь 
«многие-ко-многим» (many-to-many) - всё как в реляционных БД"""
