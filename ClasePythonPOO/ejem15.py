# herencia
class A:
    def hola(self):
        print("Hola heredo de la clase A")


class B:
    def hola(self):
        print("Hola heredo de la clase B")


class C(B, A):
    pass


obj = C()
obj.hola()
