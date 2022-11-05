from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from messagebox import msg_error, msg_about
import pymysql as sql
import db

app = QtWidgets.QApplication([])


login = uic.loadUi("untitled.ui")
registro = uic.loadUi("registro.ui")
registro_tutor = uic.loadUi("registro_profesor.ui")
entrar= uic.loadUi("entrar.ui")

db=db.Database()

def gui_login():
    correo = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(correo) == 0 or len(password)==0:
        login.label_4.setText("Ingrese todos los datos")
    else:
        rs=db.login_alumno(correo, password) 
        if rs:
            msg_about("","Se pudo iniciar sesión con éxito")
            gui_entrar()
        else:
            msg_error("Error", "El correo o la contraseña no son correctos")

def gui_registro_alumno():
    login.hide()
    registro.show()

def gui_entrar():
    login.hide()
    entrar.show()

def gui_volver_login():
    registro.hide()
    registro_tutor.hide()
    login.label_4.setText("")
    login.show()

def gui_registro_tutor():
    login.hide()
    registro_tutor.show()
    
def datos_alumno():
    nombre = registro.lineEdit.text()
    apellido = registro.lineEdit_2.text()
    correo = registro.lineEdit_3.text()
    aula = registro.comboBox.currentText()
    contraseña = registro.lineEdit_5.text()
    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
        db.registro_alumno(nombre, apellido, correo, contraseña, aula)
        msg_about("Éxito", "Se ha registrado al alumno correctamente")
        registro.lineEdit.setText("")
        registro.lineEdit_2.setText("")
        registro.lineEdit_3.setText("")
        registro.lineEdit_5.setText("")

def datos_tutor():
    nombre = registro_tutor.lineEdit.text()
    apellido = registro_tutor.lineEdit_2.text()
    correo = registro_tutor.lineEdit_3.text()
    aula = registro_tutor.comboBox.currentText()
    contraseña = registro_tutor.lineEdit_5.text()

    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
        db.registro_tutor(nombre, apellido, aula, correo, contraseña)
        msg_about("Éxito", "Se ha registrado al tutor correctamente")
        registro_tutor.lineEdit.setText("")
        registro_tutor.lineEdit_2.setText("")
        registro_tutor.lineEdit_3.setText("")
        registro_tutor.lineEdit_5.setText("")

def cerrar():
    app.exit()

 
login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(gui_registro_alumno)    
login.pushButton_4.clicked.connect(gui_registro_tutor)

registro.pushButton.clicked.connect(datos_alumno)
registro.pushButton.clicked.connect(gui_registro_alumno)
registro.pushButton_3.clicked.connect(gui_volver_login)

registro_tutor.pushButton_3.clicked.connect(datos_tutor)
registro_tutor.pushButton_3.clicked.connect(gui_registro_tutor)
registro_tutor.pushButton_2.clicked.connect(gui_volver_login)

login.show()
app.exec_()
