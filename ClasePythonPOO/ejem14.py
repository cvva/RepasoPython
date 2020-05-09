# encapsulacion
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde afuera"

    def atributo_publico(self):
        return self.__atributo_privado

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde afuera")

    def metodo_publico(self):
        return self.__metodo_privado()


e = Ejemplo()
e.metodo_publico()
print(e.atributo_publico())
