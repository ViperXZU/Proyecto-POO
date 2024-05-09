from model.usuario import User

while True:
    print("Bienvenido al sistema de gestion de Empresa")
    print("Por favor, ingrese su usuario y contraseña")
    nombre = input("Usuario: ")
    contrasena = input("Contraseña: ")
    usuario = User(nombre, contrasena)
    if nombre == usuario.nombre and contrasena == usuario.password:
        print("Bienvenido al sistema")
        break
    else:
        print("Usuario o contraseña incorrectos")
        print("Por favor, vuelva a intentarlo")
        print("")

