from conex import conn
import traceback

class daoUser:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "adminbase", "colocolo", "encodertask")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn
    
    def validarLogin(self,user):
        sql = "select username, password from user where username = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.username,))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
        
        return resultado    

    def listarEmpleados(self):

        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select nombre,apellido,correo,telefono,salario,fecha_inicio,direccion from empleado")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            c.closeConex()

        return result

    def buscarEmpleado(self, user):
        sql = "select id,nombre,apellido,correo,telefono,salario,fecha_inicio,direccion from empleado where lower(nombre) = %s"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.nombre,))
            #fetchone, rescata del curso una sola fila (tupla)
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
        return resultado


    def borrarDepartamentoIdEmpleados(self, empleado):
        sql = "UPDATE empleado SET id_departamento = NULL WHERE id = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, empleado.id)
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
                
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
            c.rollback()
        finally:
            c.closeConex()
        return mensaje

    def actualizarEmpleado(self, empleado, opc):
        """opc es la opcion que se desea modificar"""
        columnas = {1: 'correo', 2: 'password', 3: 'salario', 4: 'telefono', 5: 'direccion'}
        columna = columnas[opc]
        if opc == 2:
            sql = "UPDATE usuario SET password = %s WHERE id_usuario = (SELECT id FROM empleado WHERE nombre = %s);"
        else:
            sql = "UPDATE empleado SET {} = %s WHERE nombre = %s".format(columna)
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (getattr(empleado, columna), empleado.nombre))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
                
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
            c.rollback()
        finally:
            c.closeConex()
        return mensaje
    
    def eliminarEmpleado(self, empleado):
        sql = "call eliminarEmpleado(%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.nombre,))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Usuario eliminado satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
            c.rollback()
        finally:
            c.closeConex()
        return mensaje
    def agregarEmpleado(self,empleado, user):
        sql = "call InsertarEmpleado_Usuario(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.nombre,empleado.apellido, empleado.correo,empleado.telefono,empleado.salario,empleado.fecha_contrato,empleado.direccion, empleado.rol,user.password))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
            c.rollback()
        finally:
            c.closeConex()
        return mensaje



