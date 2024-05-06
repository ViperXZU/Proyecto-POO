import pymysql

conexion = None

conexion=pymysql.connect(user="viperxzu", password="Dec211..--", 
                host="proyectos-u-azure-mysql.mysql.database.azure.com", 
                port=3306, database="baseviper", ssl_ca="DigiCertGlobalRootCA.pem", 
                ssl_disabled=False)

if conexion is not None :print("Hola mundo")
