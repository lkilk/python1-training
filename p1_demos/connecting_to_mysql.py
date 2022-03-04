import pymysql

dbconn = pymysql.connect(host="localhost",user="user1",password="Letmein_1")

dbcursor = dbconn.cursor()

dbcursor.execute("use sat")

dbcursor.execute("insert into department VALUES(50 , 'Training','Croydon')")

query = "SELECT * FROM department"

dbcursor.execute(query)

for row in dbcursor:
    print(row)

dbcursor.close()

dbconn.commit()
dbconn.close()
