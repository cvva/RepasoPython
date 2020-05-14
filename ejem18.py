from ejem17 import Conexion
# sentencia para mostrar los paises de la BD sakila
try:
    cn = Conexion('localhost', 'root', '', 'sakila')
    sql = "SELECT * FROM country"
    cursor = cn.ejecutar_sentencia(sql)
    paises = cursor.fetchall()
    for pais in paises:
        print("ID : ", pais[0])
        print("Pais :", pais[1])
        print("fecha: ", pais[2])
        print("_______________\n")
except Exception as e:
    cn.rollback()
    print(e)
finally:
    cn.cerrar_conexion()
