import mysql.connector
from my_sql_password import PASS

"""Мы установили на машину MySQL, и используя командную строку создали БД - sampledb.
В ней мы создали три таблицы: emps, salary, orders и столбцы в них.
Теперь заполним эти таблицы используя библиотеку mysql-connector-python"""

try:
	cnx = mysql.connector.connect(user='root', password=PASS, host='127.0.0.1', database='sampledb')
	cursor = cnx.cursor()

	# объявление строк с сотрудниками
	emps = [
		(9001, "Jeff Russell", "sales"),
		(9002, "Jane Boorman", "sales"),
		(9003, "Tom Heints", "sales")
	]

	# объявление запроса
	query_add_emp = ("""INSERT INTO emps (empno, empname, job) VALUES (%s, %s, %s)""")

	# вставка строк с сотрудниками
	for emp in emps:
		cursor.execute(query_add_emp, emp)

	# определение и вставка размеров оклада
	salary = [
		(9001, 3000),
		(9002, 2800),
		(9003, 2500)
	]

	query_add_salary = ("""INSERT INTO salary (empno, salary) VALUES (%s, %s)""")
	for sal in salary:
		cursor.execute(query_add_salary, sal)

	# объявление и вставка заказов
	orders = [
		(2608, 9001, 35),
		(2617, 9001, 35),
		(2620, 9001, 139),
		(2621, 9002, 95),
		(2626, 9002, 218)
	]

	query_add_order = ("""INSERT INTO orders(pono, empno, total) VALUES (%s, %s, %s)""")
	for order in orders:
		cursor.execute(query_add_order, order)

	# делаем вставку в БД постоянной
	cnx.commit()

except mysql.connector.Error as err:
	print("Error-Code:", err.errno)
	print("Error-Message: {}".format(err.msg))

finally:
	cursor.close()
	cnx.close()



