# Python con BD MySQl
# comando -> pip install pymsql
import pymysql

db = pymysql.connect('localhost', 'root', '', 'sakila')
print(db)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)

sql = "SELECT * FROM country"
cursor.execute(sql)
paises = cursor.fetchall()
for pais in paises:
    print("ID : ", pais[0])
    print("Pais :", pais[1])
    print("fecha: ", pais[2])
    print("_______________\n")

sql = "INSERT INTO country (country, last_update) VALUES ('Country Prueba',now())"
cursor.execute(sql)
db.commit()
