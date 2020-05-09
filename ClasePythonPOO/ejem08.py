from ejem07 import Persona
from ejem09 import Instructor

class Estudiante(Persona, Instructor):
    
    def saludar(self):
        print("Hola yo soy el estudiante " + self.nombre)

    def mostrarEdad(self, edad):
        print("Edad "+ edad)