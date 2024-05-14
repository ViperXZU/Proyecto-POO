from conex import conn
import traceback

class daoDepartamento:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "adminbase", "colocolo", "encodertask")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn
    
    def listarDepartamentos(self):
        sql = "select dep.id, dep.nombre, emp.nombre from departamento dep inner join empleado emp on dep.id_gerente = emp.id;"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            #fetchone, rescata del curso una sola fila (tupla)
            resultado = cursor.fetchall()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
        return resultado
    
    def listarEmpleadosDepartamento(self, departamento):
        sql = "select emp.id, emp.nombre, emp.apellido, emp.correo, emp.telefono, emp.salario, emp.fecha_inicio, emp.direccion from empleado emp inner join departamento dep on emp.id_departamento = dep.id where lower(dep.nombre) like %s;"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (departamento.nombre.lower()))
            #fetchone, rescata del curso una sola fila (tupla)
            resultado = cursor.fetchall()

        except Exception as ex:
            print(traceback.print_exc())
            c.rollback()
        finally:
            c.closeConex()
        return resultado


    def buscarDepartamento(self, departamento):
        sql = "select dep.id, dep.nombre, emp.nombre from departamento dep inner join empleado emp on dep.id_gerente = emp.id where lower(dep.nombre) like %s;"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (departamento.nombre.lower()))
            #fetchone, rescata del curso una sola fila (tupla)
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
        return resultado

    def eliminarDepartamento(self, departamento):
        sql = "delete from departamento where lower(nombre) like %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (departamento.nombre.lower()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos eliminados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            c.rollback()
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            c.closeConex()
        return mensaje
    

    def agregarDepartamento(self,departamento):
        sql = "insert into departamento (nombre, id_gerente) values (%s, %s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (departamento.nombre, departamento.gerente.id))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            c.closeConex()
        return mensaje 
    
    def actualizarDepartamento(self,departamento_old, departamento_nuevo,opc):
        columnas = {1: 'nombre', 2: 'gerente'}
        if opc == 2:
            sql = "update departamento set id_gerente = %s where lower(nombre) like %s".format(columnas[opc])
        else:
            sql = "update departamento set {} = %s where lower(nombre) like %s".format(columnas[opc])
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (getattr(departamento_nuevo, columnas[opc]), departamento_old.nombre.lower()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            c.closeConex()
        return mensaje
    
    