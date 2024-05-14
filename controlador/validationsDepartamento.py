from controlador.dto_departamento import DepartamentoDTO
from controlador.dto_user import UserDTO
from utils.utilsfunctions import isEmpty   


def listarDepartamentos():
    resu = DepartamentoDTO().listarDepartamentos()
    if resu is not None:
        for r in resu:
            print(r)
    else:
        print("No hay departamentos registrados")

def validateFindDepartamento():
    nombre = input("Ingrese el nombre del departamento a buscar : ")
    if isEmpty(nombre):
        return validateFindDepartamento()
    
    resu = DepartamentoDTO().buscarDepartamento(nombre)

    if resu is not None:
        print(resu)
    else:
        print("Usuario No encontrado")

def validaDelDepartamento():

    nombre = input("Ingrese el nombre del departamento a eliminar : ")
    if isEmpty(nombre):
            return validaDelDepartamento()
        
    resu = DepartamentoDTO().buscarDepartamento(nombre)
    if resu is not None:
        print("Datos --> ", resu)
        respuesta = input("Esta seguro de la eliminación [s/n]: ") #crear función para validar respuesta
        if respuesta == "s":
            print(DepartamentoDTO().eliminarDepartamento(nombre))
        elif respuesta == "n":
            return
        else:
            print("Opción no válida")
            return validaDelDepartamento()
    else:
        print("Usuario No encontrado")


def validateUpdateDepartamento():
    nombre = input("Ingrese el nombre del departamento a modificar : ")
    if isEmpty(nombre):
        return validateUpdateDepartamento()
    #trae devuelta un objeto User
    resu = DepartamentoDTO().buscarDepartamento(nombre)
    if resu is not None:
        print("Datos --> ", resu)

        print("Que datos desea modificar?")
        print("1. Nombre")
        print("2. Gerente")
        try:
            opc = int(input("Ingrese una opción : "))
        except ValueError:
            print("Debe ingresar un valor numérico")
            return validateUpdateDepartamento()

        if opc == 1:
            nombre_nuevo = input("Ingrese el nuevo nombre: ")
            if isEmpty(nombre_nuevo):
                return validateUpdateDepartamento()
            print(DepartamentoDTO().actualizarDepartamento(nombre, nombre_nuevo, opc))
        elif opc == 2:
            gerente_nuevo = input("Ingrese el nuevo gerente: ")
            if isEmpty(gerente_nuevo):
                return validateUpdateDepartamento()
            resu = UserDTO().buscarEmpleado(gerente_nuevo)
            if resu is not None:
                print(resu)
                if input("Confirmar gerente [s/n]: ") == "s":
                    print(DepartamentoDTO().actualizarDepartamento(nombre, resu.id, opc))
                else:
                    return validateUpdateDepartamento()
            else:
                print("Usuario No encontrado")
                return validateUpdateDepartamento()
    else:
        print("Usuario No encontrado")


def validateAddDepartamento():
    nombre = input("Ingrese nombre del departamento a incorporar: ")
    if isEmpty(nombre):
        return validateAddDepartamento()
    #trae un objeto usuario
    resu = DepartamentoDTO().buscarDepartamento(nombre)
    if resu is not None:
        """Si el departamento ya existe, se muestra el departamento y se pregunta si se desea confirmar la creación"""
        print("Este Departamento ya existe:\n", resu)
        return validateAddDepartamento()
    else:
        nombre_gerente = input("Ingrese nombre del gerente: ")
        if isEmpty(nombre_gerente):
            return validateAddDepartamento()
        resu = UserDTO().buscarEmpleado(nombre_gerente);
        if resu is not None:
            print(resu)
            if input("Confirmar gerente [s/n]: ") == "s":
                print(DepartamentoDTO().agregarDepartamento(nombre, resu))
            else:
                return validateAddDepartamento()
        else:
            print("Usuario No encontrado")
            return validateAddDepartamento()

def menuDepartamento():
    print("1. Listar Departamentos")
    print("2. Agregar Departamento")
    print("3. Eliminar Departamento")
    print("4. Actualizar Departamento")
    print("5. Buscar Departamento")
    print("6. Asignar Empleado a Departamento")
    print("7. Volver al menú principal")
    try:
        opc = int( input("Ingrese una opción : "))
        return opc
    except ValueError:
        print("Debe ingresar un valor numérico")
        return menuDepartamento()

def inicialDepartamento():
    while True:
        opc = menuDepartamento()
        if opc == 1:
            listarDepartamentos()
        elif opc == 2:
            validateAddDepartamento()
        elif opc == 3:
            validaDelDepartamento()
        elif opc == 4:
            validateUpdateDepartamento()
        elif opc == 5:
            validateFindDepartamento()
        elif opc == 6:
            print("En construcción")
        elif opc == 7:
            return
        else:
            print("Opción no válida")

