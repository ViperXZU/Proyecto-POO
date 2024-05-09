from usuario import User
from contrato import Contrato
import datetime

class Empleado(User):
    direccion = ""
    telefono = ""
    email = ""
    contrato = None
    def __init__(self, nombre,  password = None, email = None, direccion = None, telefono= None, sueldo = None, fecha_inicio = datetime.datetime.now()):
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        super().__init__(nombre, password)
        self.contrato = Contrato(sueldo, fecha_inicio)

    def __str__(self):
        return super().__str__() + " Email: " + self.email + " Dirección: " + self.direccion + " Teléfono: " + self.telefono + " Contrato: " + self.contrato.__str__()
    


