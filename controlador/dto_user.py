from modelo.empleado import Empleado
from modelo.user import User    
from dao.dao_user import daoUser
from utils.encoder import Encoder

class UserDTO:

    def listarEmpleados(self):
        daouser = daoUser()
        resultado = daouser.listarEmpleados()
        lista = []
        if resultado is not None:
            for u in resultado:
                usuario = Empleado(nombre=u[0], apellido=u[1], email=u[2], telefono=u[3]
                                   , salario=u[4], fecha_contrato=u[5], direccion=u[6])
                lista.append(usuario)
        return lista

    def buscarEmpleado(self, username):
        daouser = daoUser()
        resultado = daouser.buscarEmpleado(User(nombre=username))
        return Empleado( id=resultado[0], nombre=resultado[1], apellido=resultado[2],
                         email=resultado[3], telefono=resultado[4], salario=resultado[5],
                         fecha_contrato=resultado[6], direccion=resultado[7]) if resultado is not None else None

    def validarLogin(self, username, clave):
        daouser = daoUser()
        resultado = daouser.validarLogin(Empleado(username=username, password=clave))
        return Empleado(resultado[0]) if resultado is not None and Encoder().decode(clave,resultado[1]) else None
    
    def actualizarEmpleado(self, username, dato_nuevo, opc):
        
        daouser = daoUser()
        if opc == 1:
            resultado = daouser.actualizarEmpleado(Empleado(nombre=username, email=dato_nuevo), opc)
        elif opc == 2:
            resultado = daouser.actualizarEmpleado(User(nombre=username, password=Encoder().encode(dato_nuevo)), opc)
        elif opc == 3: 
            resultado = daouser.actualizarEmpleado(Empleado(nombre=username, salario=dato_nuevo), opc)
        elif opc == 4:
            resultado = daouser.actualizarEmpleado(User(nombre=username, telefono=dato_nuevo), opc)
        elif opc == 5:
            resultado = daouser.actualizarEmpleado(Empleado(nombre=username, direccion=dato_nuevo), opc)
        else:
            resultado = "Opción no válida"
        return resultado
    
    def eliminarEmpleado(self, username):
        daouser = daoUser()
        resultado = daouser.eliminarEmpleado(Empleado(nombre=username))
        return resultado
    
    def agregarEmpleado(self, username, apellido, email, password, telefono, direccion, salario, rol=1):
        daouser = daoUser()
        resultado = daouser.agregarEmpleado(Empleado(nombre=username, apellido=apellido, email=email,
                                                     telefono=telefono, direccion=direccion, salario=salario, rol=rol),
                                                     User(password=Encoder().encode(password)))
        return resultado
    
