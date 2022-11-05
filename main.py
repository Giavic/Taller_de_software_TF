from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from messagebox import msg_error, msg_about
import pymysql as sql
import db

app = QtWidgets.QApplication([])


login = uic.loadUi("untitled.ui")
registro = uic.loadUi("registro.ui")
registro_profesor = uic.loadUi("registro_profesor.ui")
entrar= uic.loadUi("entrar.ui")


db=db.Database()


def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(name) == 0 or len(password)==0:
        login.label_4.setText("Ingrese todos los datos")
    else:
        rs=db.login_alumno(name, password)

        if rs:
            msg_about("","Se pudo iniciar sesión con éxito")
            gui_entrar()
        else:
            msg_error("Error", "El usuario o la contraseña no son correctos")


def gui_registro_alumno():
    nombre = registro.lineEdit.text()
    apellido = registro.lineEdit_2.text()
    correo = registro.lineEdit_3.text()
    aula = registro.lineEdit_4.text()
    contraseña = registro.lineEdit_5.text()

    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
        db.registro_alumno(nombre, apellido, correo, contraseña, aula)
        msg_about("Éxito", "Se ha registrado al alumno correctamente")
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
    nombre = registro.lineEdit.text()
    apellido = registro.lineEdit_2.text()
    correo = registro.lineEdit_3.text()
    aula = registro.lineEdit_4.text()
    contraseña = registro.lineEdit_5.text()

    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
        db.registro_tutor(nombre, apellido, aula, correo, contraseña)
        msg_about("Éxito", "Se ha registrado al tutor correctamente")
        registro.lineEdit.setText("")
        registro.lineEdit_2.setText("")
        registro.lineEdit_3.setText("")
        registro.lineEdit_4.setText("")
        registro.lineEdit_5.setText("")
    

def gui_registro():
    login.hide()
    registro.show()

def cerrar():
    app.exit()



login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(gui_registro)    
login.pushButton_3.clicked.connect(cerrar)
login.pushButton_4.clicked.connect(gui_registro_profesor)
registro.pushButton.clicked.connect(gui_registro_alumno)
registro.pushButton_2.clicked.connect(cerrar) 
registro.pushButton_3.clicked.connect(gui_volver_login)
registro_profesor.pushButton.clicked.connect(cerrar)   
registro_profesor.pushButton_2.clicked.connect(gui_volver_login)

login.show()
app.exec_()
