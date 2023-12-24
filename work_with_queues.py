'''Импортируем объект deque который позволяет создавать очереди (FIFO - first in first out)'''
from collections import deque

# имеется исходный список задач tasks_list и выводим его
tasks_list = ['Pay bills', 'Tidy up', 'Walk the dog', 'Cook dinner']
print(tasks_list)

# преобразуем список task_list в очередь task_queue (передаем task_list в deque)
task_queue = deque(tasks_list)

# добавляем задачу к очереди
task_queue.append('Wash the car')

# методом .popleft удаляем из очереди первую задачу и выводим сообщение, что эта задача - Done!
print(task_queue.popleft(), ' - Done!')

# преобразуем очередь task_queue обратно к списку и помещаем в новую переменную updated_task_list
updated_task_list = list(task_queue)

# выводим обновленный список задач
print(updated_task_list)
