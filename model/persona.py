from usuario import Usuario

class Persona(Usuario):
    
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return super().__str__() + f'Persona({self.nombre}, {self.apellido}, {self.correo}, {self.telefono})'