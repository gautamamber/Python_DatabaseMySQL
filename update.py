import MySQLdb
db = MySQLdb.connect('localhost','root','amber','unix')
cursor = db.cursor()
sql = """UPDATE EMPLOYEE SET AGE = 22
WHERE ID = 2;"""
cursor.execute(sql)
db.commit()
print("done")
db.close()