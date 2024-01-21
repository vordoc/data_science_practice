import mysql.connector
from my_sql_password import PASS

"""   --- Запрос к базе данных ---
Теперь, когда мы заполнили таблицы информацией, можно запросить эти данные, чтобы дальше использовать их в коде. 
Допустим, требуется получить все строки из таблицы emps, где значение поля empno больше 9001. 
Для этого в качестве образца будем использовать скрипт из предыдущего раздела, 
изменив только блок try"""

try:
	cnx = mysql.connector.connect(user='root', password=PASS, host='127.0.0.1', database='sampledb')
	cursor = cnx.cursor()
	# запрос к БД
	query = ("SELECT * FROM emps WHERE empno > %s")
	empno = 9001
	cursor.execute(query, (empno,))
	for (empno, empname, job) in cursor:
		print(f"{empno}, {empname}, {job}")

except mysql.connector.Error as err:
	print("Error-Code:", err.errno)
	print("Error-Message: {}".format(err.msg))

finally:
	cursor.close()
	cnx.close()


print('\n--------------------------------------------------------------------\n')


"""Можно написать инструкции SELECT, которые объединяют строки из разных таблиц. Объединение таблиц реляционной 
базы данных повторяет процесс объединения датафреймов pandas, который был описан в главе 3. 
Обычно таблицы объединяются с помощью отношений внешнего ключа, определяемого при настройке базы данных.
Предположим, что необходимо объединить таблицы emps и salary, сохраняя условие о том, что значение empno 
должно быть больше 9001. Мы делаем это через их общие столбцы (empno), поскольку определили это поле в таблице 
salary как внешний ключ, ссылающийся на empno в таблице emps."""
try:
	cnx = mysql.connector.connect(user='root', password=PASS, host='127.0.0.1', database='sampledb')
	cursor = cnx.cursor()
	# запрос к БД
	query = ("""SELECT e.empno, e.empname, e.job, s.salary FROM emps e JOIN salary s ON e.empno = s.empno 
	WHERE e.empno > %s""")
	empno = 9001
	cursor.execute(query, (empno,))
	for (empno, empname, job, salary) in cursor:
		print(f"{empno}, {empname}, {job}, {salary}")

except mysql.connector.Error as err:
	print("Error-Code:", err.errno)
	print("Error-Message: {}".format(err.msg))

finally:
	cursor.close()
	cnx.close()


print('\n--------------------------------------------------------------------\n')


"""объединим строки из таблиц emps и orders"""
try:
	cnx = mysql.connector.connect(user='root', password=PASS, host='127.0.0.1', database='sampledb')
	cursor = cnx.cursor()
	# запрос к БД
	query = ("""SELECT e.empno, e.empname, e.job, o.total 
	FROM emps e JOIN orders o 
	ON e.empno = o.empno WHERE e.empno > %s""")
	empno = 9001
	cursor.execute(query, (empno,))
	for (empno, empname, job, total) in cursor:
		print(f"{empno}, {empname}, {job}, {total}")

except mysql.connector.Error as err:
	print("Error-Code:", err.errno)
	print("Error-Message: {}".format(err.msg))

finally:
	cursor.close()
	cnx.close()


