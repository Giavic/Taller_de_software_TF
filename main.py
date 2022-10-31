from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from messagebox import msg_error, msg_about
import sqlite3 as sql

app = QtWidgets.QApplication([])


login = uic.loadUi("untitled.ui")
registro = uic.loadUi("registro.ui")
registro_profesor = uic.loadUi("registro_profesor.ui")
entrar= uic.loadUi("entrar.ui")


try:
    con = sql.connect("base de datos.db")
    con.commit()
    con.close()
except:
    print("Error en la base de datos...")


def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(name) == 0 or len(password)==0:
        login.label_4.setText("Ingrese todos los datos")
    else:
        con = sql.connect("base de datos.db")
        cursor = con.cursor()
        cursor.execute('SELECT usuario, contraseña FROM users WHERE usuario = ? AND contraseña = ?' ,(name, password))

        if cursor.fetchall():
            msg_about("","Se pudo iniciar sesión con éxito")
            gui_entrar()
        else:
            msg_error("Error", "El usuario o la contraseña no son correctos")


def crear_tabla():
    con = sql.connect("base de datos.db")
    cursor = con.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users (
            nombres text,
            apellidos text,
            correo text,
            usuario text,
            contraseña text
        )"""
    )

    con.commit()
    con.close()

def registrar(nombres, apellidos, correo, usuario, contraseña):
    con = sql.connect("base de datos.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO users VALUES ('{nombres}', '{apellidos}', '{correo}', '{usuario}', '{contraseña}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def datos():
    nombres = registro.lineEdit.text()
    apellidos = registro.lineEdit_2.text()
    correo = registro.lineEdit_3.text()
    usuario = registro.lineEdit_4.text()
    contraseña = registro.lineEdit_5.text()

    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
        registrar(nombres, apellidos, correo, usuario, contraseña)
        msg_about("Éxito", "Se ha registrado el alumno correctamente")
        registro.lineEdit.setText("")
        registro.lineEdit_2.setText("")
        registro.lineEdit_3.setText("")
        registro.lineEdit_4.setText("")
        registro.lineEdit_5.setText("")


def gui_entrar():
    login.hide()
    entrar.show()

def gui_volver_login():
    registro.hide()
    login.label_4.setText("")
    login.show()

def gui_registro_profesor():
    login.hide()
    registro_profesor.show()
    

def gui_registro():
    login.hide()
    registro.show()
    crear_tabla()

def cerrar():
    app.exit()



login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(gui_registro)    
login.pushButton_3.clicked.connect(cerrar)
login.pushButton_4.clicked.connect(gui_registro_profesor)
registro.pushButton.clicked.connect(datos)
registro.pushButton_2.clicked.connect(cerrar) 
registro.pushButton_3.clicked.connect(gui_volver_login)
registro_profesor.pushButton.clicked.connect(cerrar)   
registro_profesor.pushButton_2.clicked.connect(gui_volver_login)

login.show()
app.exec_()
