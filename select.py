import MySQLdb
db = MySQLdb.connect('localhost','root','amber','unix')
cursor = db.cursor()
sql = """SELECT * FROM EMPLOYEE;"""
try:
	cursor.execute(sql)
	result = cursor.fetchall()
	for row in result:
		ID = row[0]
		NAME = row[1]
		SEX = row[2]
		AGE = row[3]
		print("ID = %d, NAME = %s, SEX = %s, AGE = %d" %(ID,NAME,SEX,AGE))
except:
	print("OOOPS SOMETHING IS WRONG")
db.close()