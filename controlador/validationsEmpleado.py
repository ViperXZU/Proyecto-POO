from controlador.dto_user import UserDTO
from utils.utilsfunctions import isEmpty   

def listAll():
    print("Listado de Usuarios")
    resultado = UserDTO().listarEmpleados()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")

def validateFindEmpleado():
    username = input("Ingrese el nombre de usuario a buscar : ")
    if username == "":
        print("Nombre de usuario incorrecto")
        return validateFindEmpleado()
    else:
        resu = UserDTO().buscarUsuario(username)
        if resu is not None:
            print(resu)
        else:
            print("Usuario No encontrado")
def validaDelEmpleado():
    username = input("Ingrese el nombre de usuario a eliminar : ")
    if len(username) == 0:
        print("Debe ingresar un nombre de usuario")
        return validaDelEmpleado()
    #trae devuelta un objeto User
    resu = UserDTO().buscarEmpleado(username)
    if resu is not None:
        print("Datos --> ", resu)
        respuesta = input("Esta seguro de la eliminación [s/n]: ") #crear función para validar respuesta
        if respuesta == "s":
            print(UserDTO().eliminarUsuario(username))

    else:
        print("Usuario No encontrado")
def validateUpdateEmpleado():
    username = input("Ingrese el nombre de usuario a modificar : ")
    if isEmpty(username):
        return validateUpdateEmpleado()
    #trae devuelta un objeto User
    resu = UserDTO().buscarEmpleado(username)
    if resu is not None:
        print("Datos --> ", resu)

        print("Que datos desea modificar?")
        print("1. Email")
        print("2. Clave")
        print("3. Salario")
        print("4. Telefono")
        print("5. Direccion")
        try:
            opc = int(input("Ingrese una opción : "))
        except ValueError:
            print("Debe ingresar un valor numérico")
            return validateUpdateEmpleado()

        if opc == 1:
            email = input("Ingrese nuevo email : ")
            if isEmpty(email):
                return validateUpdateEmpleado()
            print(UserDTO().actualizarEmpleado(username, email, opc))
        elif opc == 2:
            password = input("Ingrese nueva clave : ")
            if isEmpty(password):
                return validateUpdateEmpleado()
            print(UserDTO().actualizarEmpleado(username, password, opc))
        elif opc == 3:  
            salario = input("Ingrese nuevo salario : ")
            if isEmpty(salario):
                return validateUpdateEmpleado()
            print(UserDTO().actualizarEmpleado(username, salario, opc))
        elif opc == 4:
            telefono = input("Ingrese nuevo telefono : ")
            if isEmpty(telefono):
                return validateUpdateEmpleado()
            print(UserDTO().actualizarEmpleado(username, telefono, opc))
        elif opc == 5:
            direccion = input("Ingrese nueva dirección : ")
            if isEmpty(direccion):
                return validateUpdateEmpleado()
            print(UserDTO().actualizarEmpleado(username, direccion, opc))
    else:
        print("Usuario No encontrado")


def validateAddEmpleado():
    username = input("Ingrese nombre del empleado a incorporar: ")
    if len(username) == 0:
        print("Debe ingresar un nombre al empleado")
        return validateAddEmpleado()
    #trae un objeto usuario
    resu = UserDTO().buscarEmpleado(username)
    if resu is not None:
        """desplegamos el usuario, por medio de __str()__
        de la clase Usuario, que se encuentra en el 
        paquete modelo"""
        print("Datos existentes--> ", resu)
    else:
        #Ingresamos el nuevo usuario
        apellido = input("Ingrese apellido : ")
        if isEmpty(apellido):
            return validateAddEmpleado()
        
        email = input("Ingrese email : ") #crear función para validar email
        if isEmpty(email):
            return validateAddEmpleado()
        
        password = input("Ingrese clave: ") #crear funci+on para valida password
        if isEmpty(password):
            return validateAddEmpleado()
        
        telefono = input("Ingrese telefono : ") #crear función para validar telefono
        if isEmpty(telefono):
            return validateAddEmpleado()
        
        direccion = input("Ingrese dirección : ")
        if isEmpty(direccion):
            return validateAddEmpleado()
        
        salario = input("Ingrese salario : ")
        if isEmpty(salario):
            return validateAddEmpleado()
        try:
            salario = float(salario)
        except ValueError:
            print("Debe ingresar un valor numérico")
            return validateAddEmpleado()

        

        es_gerente = input("Es gerente [s/n]: ").lower()
        if es_gerente == "s":
            print(UserDTO().agregarEmpleado(username,apellido, email,password,telefono,direccion,salario,1))
        elif es_gerente == "n":
            print(UserDTO().agregarEmpleado(username,apellido, email,password,telefono,direccion,salario))
        else:
            print("Opción no válida")
            return validateAddEmpleado()



def menuEmpleados():
    print("1. Listar Empleados")
    print("2. Agregar Empleado")
    print("3. Eliminar Empleado")
    print("4. Actualizar Empleado")
    print("5. Buscar Empleado")
    print("6. Volver al menú principal")
    try:
        opc = int( input("Ingrese una opción : "))
    except ValueError:
        print("Debe ingresar un valor numérico")
        return menuEmpleados()
    return opc
### para llegar al menu primero hay que loguearse


def inicialEmpleados():
    while True:
        opc = menuEmpleados()
        if opc == 1:
            listAll()
        elif opc == 2:
            validateAddEmpleado()
        elif opc == 3:
            validaDelEmpleado() 
            
        elif opc == 4:
            validateUpdateEmpleado()
        elif opc == 5:
            validateFindEmpleado()
        elif opc == 6:
            return
        else:
            print("Opción no válida")

