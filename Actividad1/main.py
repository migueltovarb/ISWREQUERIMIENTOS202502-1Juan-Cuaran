from contacto import contacto

class ConnectMe:
    def __init__(self):
        self.lista_contactos =[]

    def RegistrarContacto (self):
        nombre = str(input("Ingrese el nombre del contacto: "))
        telefono = str(input("Ingrese el telefono del contacto: "))
        correoC = str(input("Ingrese el correo del contacto: "))
        for i in self.lista_contactos:
            if i.correo == correoC:
                print( "Error el correo ya esta asignado a otro contacto")
                return 
            
        cargo = str(input("Ingrese el cargo del contacto: "))
        contact = contacto(nombre, telefono, correoC, cargo)        
        self.lista_contactos.append(contact)

    def Listar_Contactos (self):
        for i in self.lista_contactos:
            print(f"{i.Mostrar_Info()}")
    
    def Buscar_Contacto_Nombre (self, Contacto_nombre):
        for i in self.lista_contactos:
            if i.nombre == Contacto_nombre:
                print(f"{i.Mostrar_Info()}")
            return "No se encuentra registrado"
        
    def Buscar_Contacto_Correo (self, correo_contacto):
        for i in self.lista_contactos:
            if i.correo == correo_contacto:
                print(f"{i.Mostrar_Info()}")
            return "No se encuentra registrado"
        
    def Eliminar_Contacto (self, correo):
        lista = self.lista_contactos
        for i in lista:
            if i.correo == correo:
                lista.remove(i)
                self.lista_contactos = lista
        return self.lista_contactos         
    def main (self):
        while (True):
            print("-" * 30 + "MENU PRINCIPAL" + "-"*30)
            print("1. Registrar Contacto")
            print("2. Listar Contactos")
            print("3. Buscar Contacto")
            print("4. Eliminar Contacto")
            print()
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                self.RegistrarContacto()
            elif opcion == 2:
                self.Listar_Contactos()
            elif opcion == 3:
                print("Desea buscar por nombre (1) o por correo (2)")
                r = int(input("Digite su opcion: "))
                if r == 1:
                    nombreC = str(input("Digite el nombre que quiere buscar: "))
                    for i in self.lista_contactos:
                        if i.nombre == nombreC:
                            self.Buscar_Contacto_Nombre(nombreC)
                        else:
                            print("Error el nombre no se encuentra registrado")                   
                if r ==2:
                    correoC = str(input("Digite el correo que quiere buscar:"))
                    for i in self.lista_contactos:
                        if i.correo == correoC:
                            self.Buscar_Contacto_Correo(correoC)
                        else:
                            print("Error el correo no se encuentra registrado")
            elif opcion == 4:
                correoCt = str(input("Digite el correo del contacto que quiere eliminar: "))
                for i in self.lista_contactos:
                    if i.correo == correoCt:
                        self.Eliminar_Contacto(correoCt)
                    else:
                            print("Error no se ha encontrado el correo")

if __name__ == "__main__":
    Empresa = ConnectMe()
    Empresa.main()