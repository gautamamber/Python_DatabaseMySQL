import MySQLdb
db = MySQLdb.connect('localhost','root','amber','unix')
cursor = db.cursor()
sql = """ INSERT INTO EMPLOYEE(ID,NAME,SEX,AGE)
VALUES(3,'kapisha','MALE',20);"""
cursor.execute(sql)
db.commit()
print("done")
db.close()