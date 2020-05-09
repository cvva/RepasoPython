# Clases y Objetos
class Persona:
    nombre = "Juan perez"
    edad = 20
    sexo = "Masculino"

    """def __init__(self, nom):
        self.nombre = nom"""

    def saludar(self):
        print("Bienvenido a la clase de POO ", self.nombre)


estudiante = Persona()
print(estudiante.saludar())
