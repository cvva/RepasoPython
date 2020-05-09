class Operaciones:
    num1 = 0
    num2 = 0

    def suma(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
        print(f"La suma es {self.num1 + self.num2}")

    def suma2(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
        return self.num1 + self.num2


numero = Operaciones()
numero.suma(5, 8)
sum = numero.suma2(5, 3)
print(f"la suma con func sum2() es {sum}")
