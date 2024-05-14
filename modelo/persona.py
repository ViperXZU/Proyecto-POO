
class Persona:
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nCorreo: " + self.correo + "\nTelefono: " + self.telefono
