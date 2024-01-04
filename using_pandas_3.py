import pandas as pd
from using_pandas_2 import emps, salary

print("\n----------------------------------------------------------\n")

"""Объединение датафреймов. 
Pandas позволяет объединять датафреймы подобно тому, как мы объединяем 
различные таблицы в реляционной базе данных. 
Это позволяет собирать данные для анализа вместе. Методы объединения, поддерживаемые структурой данных 
DataFrame, напоминают операции при работе с базами данных: merge() и join(). 
Эти методы содержат несколько разных параметров, но так или иначе могут 
выступать как взаимозаменяемые"""


"""метод join предназначен для простого объединения датафреймов на основании их 
индексов. В этом конкретном примере нам даже не нужно было предоставлять 
дополнительные параметры; объединение по индексу — поведение по умолчанию. 
В результате получаем следующий датасет:"""

emps_salary = emps.join(salary)
print(emps_salary)

print("\n----------------------------------------------------------\n")

"""На практике бывает необходимо объединить два датафрейма, в одном из которых 
есть строки, не имеющие совпадений в другом датафрейме. 
Предположим, у нас есть еще одна строка в датафрейме emps, а в salary соответствующей строки нет.
В этом случае создадим объект pandas Series, а затем добавим его к датафрейму 
emps с помощью метода append()."""

new_emp = pd.Series({'Name': 'John Hardy', 'Job': 'sales'}, name=9004)
emps = emps._append(new_emp)
print(emps)

print("\n----------------------------------------------------------\n")

emps_salary = emps.join(salary)
print(emps_salary)

print("\n----------------------------------------------------------\n")

"""Обратите внимание: строка, добавленная в emps, появляется в итоговом датасете, 
даже если в salary нет связанной с ней строки. 
Запись NaN в поле Salary последней строки означает, что значение оклада отсутствует. 
В некоторых случаях пустые значения в строках допустимы, как в данном примере, однако
в других ситуациях может понадобиться исключить строки, которые не имеют
соответствий в другом датафрейме.

По умолчанию метод join() использует индексы вызывающего датафрейма
в результирующем, объединенном датафрейме, выполняя таким образом left join. 

В примере выше вызывающим датафреймом был emps. 
Он считается левым датафреймом в операции объединения, и поэтому все строки из него включаются в результирующий датасет. 

Это поведение можно изменить, передав параметр how в метод join(). 
Данный параметр принимает следующие значения:

left - Использует столбец с индексами вызывающего датафрейма (или
другой столбец, если указан параметр on), возвращая все строки из вызывающего (левого) датафрейма и только совпадающие строки из другого
(правого) датафрейма.

right - Использует индекс другого (правого) датафрейма, возвращая из
него все строки и только совпадающие строки из вызывающего (левого)
датафрейма.

outer - Создает комбинацию индексов вызывающего датафрейма (или
иного столбца, если указан параметр on) и индексов другого датафрейма,
возвращая все строки из обоих датафреймов.

inner - Формирует пересечение индексов вызывающего датафрейма (или
иного столбца, если указан параметр on) с индексами другого датафрейма,
возвращая только те строки, индексы которых встречаются в обоих датафреймах."""


"""Если необходимо, чтобы итоговый датафрейм включал только те строки из
emps, которые имеют соответствия в salary, выберите значение inner для параметра how в методе join():"""

emps_salary = emps.join(salary, how='inner')
print(emps_salary)






