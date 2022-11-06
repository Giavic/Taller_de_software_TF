from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from messagebox import msg_error, msg_about
import pymysql as sql
import db
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication([])


login = uic.loadUi("untitled.ui")
registro = uic.loadUi("registro.ui")
registro_tutor = uic.loadUi("registro_profesor.ui")
entrar= uic.loadUi("entrar.ui")
entrar_tutor= uic.loadUi("entrar_tutor.ui")

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
            gui_entrar(rs)
        else:
            rs=db.login_tutor(correo, password)
            if rs:
                msg_about("","Se pudo iniciar sesión con éxito")
                gui_entrar_tutor(rs)
            else:
                login.label_4.setText("Correo o contraseña incorrectos")

def gui_registro_alumno():
    login.hide()
    registro.show()

def gui_entrar(result):
    login.hide()
    entrar.show()
    entrar.label.setText(("Bienvenido alumno "+result[1]+" "+result[2]).upper())
    rs=db.mostrar_reportes(result[0])
    row=0
    while(row<len(rs)):
        entrar.tableWidget_2.insertRow(row)
        numero=QTableWidgetItem(str(row+1))
        comentario=QTableWidgetItem(str(rs[row][1]))
        fecha= QTableWidgetItem(str(rs[row][2]))
        entrar.tableWidget_2.setItem(row,0,numero)
        entrar.tableWidget_2.setItem(row,1,comentario)
        entrar.tableWidget_2.setItem(row,2,fecha)
        row+=1


def gui_entrar_tutor(result):
    login.hide()
    entrar_tutor.show()
    entrar_tutor.label.setText(("Bienvenido tutor "+result[1]+" "+result[2]).upper())

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

def bloquear_tablas():
    entrar.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    entrar.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    entrar.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    entrar.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    entrar.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    entrar.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    entrar.tableWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

bloquear_tablas()

login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(gui_registro_alumno)    
login.pushButton_4.clicked.connect(gui_registro_tutor)

registro.pushButton.clicked.connect(datos_alumno)
registro.pushButton.clicked.connect(gui_registro_alumno)
registro.pushButton_3.clicked.connect(gui_volver_login)

registro_tutor.pushButton_3.clicked.connect(datos_tutor)
registro_tutor.pushButton_3.clicked.connect(gui_registro_tutor)
registro_tutor.pushButton_2.clicked.connect(gui_volver_login)

entrar.pushButton_2.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_asistencia))
entrar.pushButton_3.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_cursos))
entrar.pushButton_8.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_mate))
entrar.pushButton_9.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_ciencias))
entrar.pushButton_10.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_comu))
entrar.pushButton_11.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_EF))
entrar.pushButton_12.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_Tuto))

entrar.pushButton_4.clicked.connect(lambda: entrar.stackedWidget.setCurrentWidget(entrar.page_reportes))

login.show()
app.exec_()
