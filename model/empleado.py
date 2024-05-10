from persona import Persona

class Empleado(Persona):
        
        def __init__(self, id, nombre, apellido, correo, telefono, salario, fecha_ingreso, direccion):
            super().__init__(nombre, apellido, correo, telefono)
            self.direccion = direccion
            self.id = id
            self.salario = salario
            self.fecha_ingreso = fecha_ingreso
        
        def __str__(self):
              return super().__str__() + f'Empleado({self.id}, {self.salario}, {self.fecha_ingreso}, {self.direccion})'