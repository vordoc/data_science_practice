"""Вспоминаем как работает абстрактная структура данных - стек (LIFO - last in, first out)"""

my_list = ['Pay bills', 'Tidy up', 'Walk the dog', 'Go to the pharmacy', 'Cook dinner']

# stack = []
#
#
# for task in my_list:
#     stack.append(task)

'''Используем однострочное формирование стека с помощью генератора списков'''
stack = [task for task in my_list]

'''Выводим построчно записи из стека, начиная с последней (метод .pop), пока он не опустеет'''
while stack:
    print(stack.pop(), ' - Done!')


print('\nThe stack is empty')

