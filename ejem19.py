from ejem17 import Conexion
# sentencia para insertar un registro en la tabla country de la BD sakila
try:
    cn = Conexion('localhost', 'root', '', 'sakila')
    # insertamos un nuevo registro
    sql = "INSERT INTO country (country, last_update) VALUES ('Country Prueba',now())"
    cursor = cn.ejecutar_sentencia(sql)
    cn.commit()
    # mostramos en pantalla los registros
    sql2 = "SELECT * FROM country"
    cursor2 = cn.ejecutar_sentencia(sql2)
    paises = cursor2.fetchall()
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
