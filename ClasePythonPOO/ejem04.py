class Estudiante:
    codigo = ""
    nombre = ""
    nota = 0

    def __init__(self, cod, nom, nota):
        self.codigo = cod
        self.nombre = nom
        self.nota = nota

    def mostrarDatos(self):
        pass


cod = input("Ingrese tu codigo : ")
nom = input("Ingrese tu nombre : ")
nota = int(input("Ingrese tu nota : "))

jose = Estudiante(cod, nom, nota)
