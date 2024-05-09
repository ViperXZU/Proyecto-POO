class User:
    nombre = ""
    email = ""
    password = ""

    def __init__(self, nombre, password = None):
        self.nombre = nombre
        self.password = password

    def __str__(self):
        return "Nombre: " + self.nombre + " Password: " + self.password
    
