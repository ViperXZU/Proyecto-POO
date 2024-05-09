
class Contrato:
    def __init__(self, fecha_inicio, sueldo = None):
        self.fecha_inicio = fecha_inicio
        self.sueldo = sueldo

    def __str__(self):
        return "Fecha de inicio de contrato: " + self.fecha_inicio + " Sueldo: " + self.sueldo