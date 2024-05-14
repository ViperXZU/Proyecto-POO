from modelo.persona import Persona

class User(Persona):
    def __init__(self,nombre=None,id= None, password= None, rol= None, apellido= None, correo= None, telefono= None):
        super().__init__(nombre, apellido, correo, telefono)
        self.id = id
        self.rol = rol
        self.password = password

    def __str__(self):
        return super().__str__() + " " + self.rol + " " + self.password

    def getId(self):
        return self.id
