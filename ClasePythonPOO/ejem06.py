#Clases, Objetos y Encapsulamiento
class Persona:

    def __init__(self, cod, name, age):
        self._codigo=cod
        self._nombre=name
        self.__edad=age
    
    def saludar(self):
        print("Hola "+ self.nombre)

jose = Persona(1,"Juan",25)
print(jose._codigo)
print(jose._nombre)
print(jose._Persona__edad)