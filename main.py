def menuAccesoUsuarios():
    print("""
||------------------------||
||  Ingreso al Sistema    ||
||------------------------||
||   Login de acceso      ||
||------------------------||
""")
   
print("\n=== Aplicación Usuarios ===\n")
menuAccesoUsuarios()

intentos = 0
while intentos < 3:
    try:
        resu= validarLogin()
    except Exception as e:
        print("Intentar Nuevamente")