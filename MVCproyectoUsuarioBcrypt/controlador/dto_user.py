from modelo.user import User
from dao.dao_user import daoUser
from utils.encoder import Encoder
from datetime import datetime

class UserDTO:

    def listarUsuarios(self):
        daouser = daoUser()
        resultado = daouser.listarUsuarios()
        lista = []
        if resultado is not None:
            for u in resultado:
                usuario = User(username=u[0], email=u[1], password=u[2], create_time=u[3])
                lista.append(usuario)
        return lista

    def buscarUsuario(self, username):
        daouser = daoUser()
        resultado = daouser.buscarUsuario(User(username=username))
        return User(resultado[0], resultado[1], resultado[2]) if resultado is not None else None

    def validarLogin(self, username, clave):
        daouser = daoUser()
        resultado = daouser.validarLogin(User(username=username, password=clave))
        return User(resultado[0]) if resultado is not None and Encoder().decode(clave,resultado[1]) else None
    def actualizarUsuario(self, username, email, password):
        daouser = daoUser()
        resultado = daouser.actualizarUsuario(User(username=username, email=email, password=Encoder().encode(password)))
        return resultado
    def eliminarUsuario(self, username):
        daouser = daoUser()
        resultado = daouser.eliminarUsuario(User(username=username))
        return resultado
    def agregarUsuario(self, username, email, password):
        daouser = daoUser()
        resultado = daouser.agregarUsuario(User(username=username, email=email, create_time= datetime.now(), password=Encoder().encode(password)))
        return resultado
    
