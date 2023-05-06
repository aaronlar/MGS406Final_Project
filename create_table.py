import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="CallLog")
cur = conn.cursor()

cmd = "CREATE TABLE Calls (\
    CallID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    Time VARCHAR(30) NOT NULL,\
    Date VARCHAR(30), \
    Out_or_In VARCHAR(30))"

cur.execute(cmd)
conn.close()
