class Padre:
    def __init__(self):
        print("Yo soy el padre")

    def metodo_padre(self):
        print("Este es un metodo padre")


class Hijo(Padre):
    def __init__(self):
        print("Yo soy el hijo")


zabala = Hijo()
zabala.metodo_padre()
