from datetime import date
from modelo.persona import Persona

class Empleado(Persona):
    def __init__(self, nombre,id = None, apellido = None, email= None, telefono= None, direccion= None, salario= None, fecha_contrato= date.today()):
        super().__init__(nombre, apellido, email, telefono)
        self.id = id
        self.direccion = direccion
        self.salario = salario
        self.fecha_contrato = fecha_contrato

    def __str__(self):
        return super().__str__() + "\nDireccion: " + self.direccion + "\nSalario: " + str(self.salario) + "\nFecha de contrato: " + str(self.fecha_contrato) + "\n "
    
    def superString(self):
        return super.__str__();


    def getId(self):
        return self.id