class Agenda:

    def __init__(self):
        self.contactos = []

    def menu(self):
        print()
        menu = [
            ['Agenda de Contactos'],
            ['==================='],
            ['1. Agregar contacto'],
            ['2. Listar contacto'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Eliminar contacto'],
            ['6. Salir']
        ]
        for x in range(7):
            print(menu[x][0])
        opcion = int(input("Seleccione una alternativa : "))

        if opcion == 1:
            # llamar al metoo Agregar
            self.agregarContacto()
        elif opcion == 2:
            # llmar al metodo Listar
            self.listarContacto()
        elif opcion == 3:
            # llamar al metodo Buscar
            self.buscarContacto()
        elif opcion == 4:
            # llamar al metodo Editar
            self.editarContacto()
        elif opcion == 5:
            # llamar al metoo Eliminar
            self.eliminarContacto()
        elif opcion == 6:
            print("Saliendo del sistema de Agenda")
            exit()
        self.menu()

    def agregarContacto(self):
        print("agregando contacto...")
        nom = input("Ingrese nombre : ")
        tel = input("Ingrese telefono : ")
        em = input("Ingrese email : ")
        self.contactos.append({'nombre': nom, 'telefono': tel, 'email': em})

    def listarContacto(self):
        print("listando contacto...")
        for val in range(len(self.contactos)):
            print(self.contactos[val]['nombre'], self.contactos[val]
                  ['telefono'], self.contactos[val]['email'])

    def buscarContacto(self):
        aux = False
        print("buscando contacto...")
        nom = input("Ingrese nombre de contacto : ")
        for val in range(len(self.contactos)):
            if nom == self.contactos[val]['nombre']:
                aux = True
                print("Contactos encontrado")
                print(self.contactos[val]['nombre'], self.contactos[val]
                      ['telefono'], self.contactos[val]['email'])
        if aux == False:
            print("Contacto no encontrado...")

    def editarContacto(self):
        print("editando contacto...")

    def eliminarContacto(self):
        print("eliminando contacto...")


contactos = Agenda()
contactos.menu()
