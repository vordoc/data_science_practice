"""Поскольку элементы множества должны быть уникальными, эта структура
данных полезна, когда нужно удалить дублирующиеся элементы из списка или
кортежа.
Предположим, что требуется просмотреть список корпоративных клиентов.
Такой список можно получить, извлекая имена клиентов из размещенных заказов.
Поскольку клиент может сделать несколько заказов, имена в списке
могут повторяться.
Такие дубликаты можно удалить с помощью множества:"""


clients_list = ['John Silver', 'Tim Jemison', 'John Silver', 'Maya Smith']

'''преобразуем список клиентов в множество и обратно в список - дубликаты имен будут убраны'''
clients_list = list(set(clients_list))

print(clients_list)



'''Чтобы сохранить первоначальный порядок элементов исходного списка, 
отсортируем множество по индексам элементов этого списка, используя sorted()'''

clients_list_1 = ['John Silver', 'Tim Jemison', 'John Silver', 'Maya Smith']

clients_list_1 = list(sorted(set(clients_list_1), key=clients_list_1.index))

print(clients_list_1)





























