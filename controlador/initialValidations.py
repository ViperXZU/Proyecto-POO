from controlador.validationsEmpleado import inicialEmpleados
from controlador.validationsDepartamento import inicialDepartamento
from controlador.dto_user import UserDTO

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    clave = input("Ingrese contraseña : ")
    resultado = UserDTO().validarLogin(username, clave)
    return resultado

def inicial():
    while True:
        print("Bienvenido al Sistema de Gestión de Empresa")
        print("Elige una opción: ")
        print("1. Gestionar Empleados")
        print("2. Gestionar Departammentos")

        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                inicialEmpleados()
            elif opcion == 2:
                inicialDepartamento()
            else:
                print("Opción no válida")
        except ValueError:
            print("Debe ingresar un valor numérico")