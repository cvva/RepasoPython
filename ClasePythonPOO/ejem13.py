class Persona:
    id = 000000
    nombres = "Estudiante prueba"
    edad = 18

    def __init__(self, name, age):
        self.nombres = name
        self.edad = age

    def __str__(self):
        return f"Hola yo soy una Persona y me llamo {self.nombres} y tambien tengo {self.edad} años"

    def saludar(self, name):
        self.nombres = name
        print("Hola yo soy ", self.nombres)


lizeth = Persona("Lizeth Ravelo", 15)
print(lizeth)
#lizeth.saludar("Lizeth Ravelo")
#lizeth.nombres="Lizeth Ravelo"
# print(lizeth.nombres)

timothy = Persona("Timothy Abad", 18)
print(timothy)
#timothy.saludar("Timothy Abad")
#timothy.nombres="Timothy Abad"
# print(timothy.nombres)
