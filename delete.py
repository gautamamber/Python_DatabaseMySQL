import MySQLdb
db = MySQLdb.connect('localhost','root','amber','unix')
cursor = db.cursor()
sql = """DELETE FROM EMPLOYEE WHERE ID = 3;"""
cursor.execute(sql)
db.commit()
print("done")
db.close()