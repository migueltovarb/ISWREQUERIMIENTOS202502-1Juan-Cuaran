class contacto:
    def __init__(self, nombre:str, telefono:str, correo:str, cargo:str):
        
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.cargo = cargo
        self.registrado = False

    def get_nombre (self):
        return self.nombre
    
    def get_telefono (self):
        return self.telefono
    
    def get_correo (self):
        return self.correo
    
    def get_cargo (self):
        return self.cargo
      
    def Mostrar_Info (self):
        return f'{self.nombre} - {self.telefono} - {self.correo} - {self.cargo}'
