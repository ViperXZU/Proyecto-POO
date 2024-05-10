from persona import Persona 

class User(Persona):
    def __init__(self, id, nombre, password, rol, apellido, correo, telefono):
        super().__init__(id, password, rol)
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        
    def __str__(self):
        return f'User({self.id}, {self.nombre}, {self.password}, {self.rol}, {self.apellido}, {self.correo}, {self.telefono})'