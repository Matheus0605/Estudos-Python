import mysql.connector 
db = mysql.connector.connect(user='root', password='',host='localhost', database='cadastro')
cursor = db.cursor(dictionary=True)

cursor.execute('select * from pessoas;')
data = cursor.fetchall()
cursor.execute('insert into pessoas values {default, "mateus"}')
db.commit()
print(data)