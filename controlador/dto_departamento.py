from modelo.departamento import Departamento
from modelo.empleado import Empleado
from dao.dao_departamento import daoDepartamento
from controlador.dto_user import UserDTO
from dao.dao_user import daoUser

class DepartamentoDTO:

    def listarEmpleadosDepartamento(self, nombre):
        daodepartamento = daoDepartamento()
        resultado = daodepartamento.listarEmpleadosDepartamento(Departamento(nombre=nombre))
        lista = []
        if resultado is not None:
            for u in resultado:
                empleado = Empleado(id=u[0], nombre=u[1], apellido=u[2], email=u[3], telefono=u[4], salario=u[5], fecha_contrato=u[6], direccion=u[7])
                lista.append(empleado)
        return lista
    
    def eliminarDepartamento(self, nombre):
        daouser = daoUser()
        daodepartamento = daoDepartamento()

        lista_empleados = self.listarEmpleadosDepartamento(nombre)

        for empleado in lista_empleados:
            daouser.borrarDepartamentoIdEmpleados(empleado)

        resultado = daodepartamento.eliminarDepartamento(Departamento(nombre=nombre))
        return resultado

    def listarDepartamentos(self):
        daodepartamento = daoDepartamento()
        resultado = daodepartamento.listarDepartamentos()
        lista = []
        if resultado is not None:
            for u in resultado:
                departamento = Departamento(id=u[0], nombre=u[1], gerente=UserDTO().buscarEmpleado(u[2]))
                lista.append(departamento)
        return lista

    def buscarDepartamento(self, nombre):
        daodepartamento = daoDepartamento()
        resultado = daodepartamento.buscarDepartamento(Departamento(nombre=nombre))
        return Departamento(id=resultado[0], nombre=resultado[1], gerente=UserDTO().buscarEmpleado(resultado[2])) if resultado is not None else None


    def agregarDepartamento(self,nombre, gerente):
        daodepartamento = daoDepartamento()
        resultado = daodepartamento.agregarDepartamento(Departamento(nombre=nombre, gerente=gerente))
        return resultado
    
    def actualizarDepartamento(self,nombre, dato_nuevo, opc):

        daodepartamento = daoDepartamento()
        if opc == 1:
            resultado = daodepartamento.actualizarDepartamento(Departamento(nombre=nombre), Departamento(nombre=dato_nuevo), opc)
        elif opc == 2:
            resultado = daodepartamento.actualizarDepartamento(Departamento(nombre=nombre), Departamento(gerente=dato_nuevo), opc)
        return resultado
    

        