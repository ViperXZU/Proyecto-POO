import pymysql

class connex:
    def __init__(self):
        try:
            self.conn = pymysql.connect(user="viperxzu", password="Dec211..--", 
                host="proyectos-u-azure-mysql.mysql.database.azure.com", 
                port=3306, database="baseviper", ssl_ca="DigiCertGlobalRootCA.pem", 
                ssl_disabled=False)
        except Exception as e:
            print("Error de conexión: ", e)
            self.conn.rollback()
            return None
    
    def closeConex(self):
        self.conn.close()

    def getConex(self):
        return self.conn

