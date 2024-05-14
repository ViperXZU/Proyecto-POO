


class Departamento:
    def __init__(self, id= None, nombre= None, gerente = None):
        self.id = id
        self.nombre = nombre
        self.__empleados = []
        self.gerente = gerente

    def __str__(self):
        return "Departamento: \nId: " + str(self.id) + "\nNombre Departamento: " + str(self.nombre) + "\nGerente: \n" + str(self.gerente) 
    
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion

    def getEmpleados(self):
        return self.empleados

    def addEmpleado(self, empleado):
        self.__empleados.append(empleado)

    def removeEmpleado(self, empleado):
        self.__empleados.remove(empleado)

    def getSalarioTotal(self):
        salario_total = 0
        for empleado in self.empleados:
            salario_total += empleado.getSalario()
        return salario_total

    def getNumeroEmpleados(self):
        return len(self.empleados)

    def getSalarioPromedio(self):
        return self.getSalarioTotal() / self.getNumeroEmpleados()