import pandas as pd

"""Библиотека pandas является фактическим стандартом для приложений Python, 
ориентированных на работу с данными (название библиотеки сложилось из фразы «Python Data Analysis Library»). 
Библиотека включает две структуры 
данных: Series (одномерную) и DataFrame (двумерную). 
Хотя DataFrame является основной структурой данных pandas, 
фактически она представляет собой коллекцию объектов Series. Поэтому важно понимать обе структуры."""



'''Series можно создать из списка'''
data = ['Jeff Russell', 'Jane Truman', 'Tom Heints']
emps_names = pd.Series(data)
print(emps_names)

print('\n-------------------------------------------------------\n')

'''Можно задать свои индексы'''
emps_names = pd.Series(data, index=[10, 11, 12])
print(emps_names)

print('\n-------------------------------------------------------\n')

'''Чтобы получить доступ к элементу в серии, укажем имя серии, а затем индекс нужного
элемента в квадратных скобках'''
print(emps_names[11])

print('\n-------------------------------------------------------\n')

'''получим срез'''
print(emps_names.loc[11:12])

print('\n-------------------------------------------------------\n')

''' Cоздадим еще одну серию emps_emails и объединим ее с серией emps_names в DataFrame'''
data_1 = ['Jeff_Russell@gmail.com', 'Jane_Truman@gmail.com', 'Tom_Heints@gmail.com']

'''присвоим новой серии те же индексы и присвоим ей имя - 'emails'''
emps_emails = pd.Series(data_1, index=[10, 11, 12], name='emails')

'''нужно присвоить имя серии emps_names, т.к. в датафрейме имена серий станут именами столбцов'''
emps_names.name = 'names'
emps_df = pd.concat([emps_names, emps_emails], axis=1)
print(emps_df)


