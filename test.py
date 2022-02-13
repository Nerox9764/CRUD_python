import mysql.connector as mysql 

try:
	con = mysql.connect(
			user = 'root',
			passwd = 'enidev911',
			port= 3306,
			db = 'inventario_python')

	cursor = con.cursor()
	sql = 'DESCRIBE curso;'
	result = cursor.execute(sql)
	print(result)
	print(con.is_connected())

except mysql.Error as err:
	print(err)

finally:
	con.close()
