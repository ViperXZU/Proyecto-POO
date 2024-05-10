from conex import conn

class daoUser:
    def __init__(self):
            try:
                self.__conn = conn.Conex("localhost", "viper", "colocolo", "viper")
                print("Conexion exitosa")
            except Exception as ex:
                print(ex)


lol = daoUser()