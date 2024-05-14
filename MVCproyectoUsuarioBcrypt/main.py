from controlador.validationsEmpleado import inicial, validarLogin


def menuAccesoUsuarios():
    print("""
||------------------------||
||  Ingreso al Sistema    ||
||------------------------||
||1. Login de acceso      ||
||2. Crear cuenta usuario ||
||------------------------||
""")
   
print("\n=== Aplicación Usuarios ===\n")
menuAccesoUsuarios()
opc = input("Ingrese opción:")
if opc == '1':
    ##### login
    intentos = 1
    while intentos <= 3:
        try:
            resu = validarLogin()
            if resu is not None:
                print(f"Bienvenido(a) Sr(a). : {resu.username}")
                inicial()
                break
            else:
                print("usuario o contraseña incorrecta")
                intentos += 1
        except:
            print("intentar nuevamente")
    if intentos == 4:
        print("contraseña boqueada")
else:
    print("en construcción")