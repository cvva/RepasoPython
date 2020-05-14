# ejm con clases y BD
import pymysql


class BaseDatos:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sakila'
        )
        self.cursor = self.connection.cursor()
        print("conexion establecida exitosmente")

    def select_all_country(self):
        sql = "SELECT * FROM country"
        try:
            self.cursor.execute(sql)
            country = self.cursor.fetchall()
            for pais in country:
                print("ID : ", pais[0])
                print("Pais :", pais[1])
                print("fecha: ", pais[2])
                print("_______________________\n")
        except Exception as e:
            print(e)

    def select_country(self, id):
        sql = "SELECT * FROM country WHERE country_id={}".format(id)
        try:
            self.cursor.execute(sql)
            country = self.cursor.fetchone()
            print("ID : ", country[0])
            print("PAIS : ", country[1])
            print("FECHA : ", country[2])
        except Exception as e:
            print(e)

    def update_country(self, id, countryname):
        sql = "UPDATE country SET country='{}' WHERE country_id={}".format(
            countryname, id)
        try:
            self.cursor.execute()
            self.connection.commit()
        except Exception as e:
            print(e)

    def close(self):
        self.connection.close()


db = BaseDatos()
db.select_all_country()
# db.select_country(90)
db.close()
