while True:
    print("Bienvenido al sistema de gestion de Empresa")
    print("Por favor, ingrese su usuario y contraseña")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    if usuario == "admin" and contrasena == "1234":
        print("Bienvenido al sistema")
        break
    else:
        print("Usuario o contraseña incorrectos")
        print("Por favor, vuelva a intentarlo")
        print("")

