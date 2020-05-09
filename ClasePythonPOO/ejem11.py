# Definimos unos cuantos clientes
clientes = [
    {'Nombre': 'George', 'Apellidos': 'De la Cruz', 'Dni': '12345678'},
    {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'Dni': '88888888'}
]

# listar los clientes
def listar_clientes():
    for c in clientes:
        print('{} {} {}'.format(c['Dni'], c['Nombre'], c['Apellidos']))
    return

# Creamos una función que muestra un cliente en una lista a partir del DNI


def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['Dni']):
            print('{} {} {}'.format(c['Dni'], c['Nombre'], c['Apellidos']))
            return
        print("Cliente no encontrado")

# Creamos una función que borra un cliente en una lista a partir del DNI


def borrar_cliente(clientes, dni):
    for i, c in enumerate(clientes):
        if (dni == c['Dni']):
            del(clientes[i])
            print("Borrado")
            return
        print("Cliente no encontrado")


# Fíjate muy bien cómo se utiliza el código estructurado
print("LISTADO DE CLIENTES")
print("===================")
print(listar_clientes())

print("MOSTRAR CLIENTE")
print("===================")
mostrar_cliente(clientes,"12345678")

print("BORRAR CLIENTE")
print("===================")
borrar_cliente(clientes,"12345678")

print("LISTADO DE CLIENTES")
print("===================")
print(listar_clientes())
