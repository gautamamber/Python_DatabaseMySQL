import MySQLdb
db = MySQLdb.connect('localhost','root','amber','unix')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)
db.close()