import MySQLdb
db = MySQLdb.connect('localhost','root','amber','unix')
cursor = db.cursor()
sql = """CREATE TABLE STUDENT (
ID INT,
NAME VARCHAR(200),
SEX VARCHAR(200),
AGE INT
);"""
cursor.execute(sql)
print("done")
db.close()