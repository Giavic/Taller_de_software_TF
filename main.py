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

def cerrar_sesion():
    entrar.hide()
    entrar_tutor.hide()
    login.lineEdit.setText("")
    login.lineEdit_2.setText("")
    login.show()
    msg_about("", "Sesión cerrada")

def gui_entrar(result):
    login.hide()
    entrar.show()
    entrar.label.setText(("Bienvenido alumno "+result[1]+" "+result[2]).upper())
    rs_reporte=db.mostrar_reportes(result[0])
    row=0
    while(row<len(rs_reporte)):
        entrar.tableWidget_2.insertRow(row)
        numero=QTableWidgetItem(str(row+1))
        comentario=QTableWidgetItem(str(rs_reporte[row][1]))
        fecha= QTableWidgetItem(str(rs_reporte[row][2]))
        entrar.tableWidget_2.setItem(row,0,numero)
        entrar.tableWidget_2.setItem(row,1,comentario)
        entrar.tableWidget_2.setItem(row,2,fecha)
        row+=1
    
    rs_nota_mate=db.mostrar_notas(result[0],"Matemática")
    rs_nota_ed=db.mostrar_notas(result[0],"Educación Física")
    rs_nota_tuto=db.mostrar_notas(result[0],"Tutoría")
    rs_nota_comu=db.mostrar_notas(result[0],"Comunicación")
    rs_nota_cien=db.mostrar_notas(result[0],"Ciencias")
    mostrar_nota_mate(rs_nota_mate)
    mostrar_nota_ed(rs_nota_ed)
    mostrar_nota_tuto(rs_nota_tuto)
    mostrar_nota_comu(rs_nota_comu)
    mostrar_nota_cien(rs_nota_cien)

# NO ABRIR XD
def mostrar_nota_mate(rs_nota):
    row=0
    while(row<4):
        tarea_b1=QTableWidgetItem(str(rs_nota[1]))
        tarea_b2=QTableWidgetItem(str(rs_nota[2]))
        tarea_b3= QTableWidgetItem(str(rs_nota[3]))
        tarea_b4= QTableWidgetItem(str(rs_nota[4]))
        bimestre1= QTableWidgetItem(str(rs_nota[5]))
        bimestre2= QTableWidgetItem(str(rs_nota[6]))
        bimestre3= QTableWidgetItem(str(rs_nota[7]))
        bimestre4= QTableWidgetItem(str(rs_nota[8]))
        parcial_b1= QTableWidgetItem(str(rs_nota[9]))
        parcial_b2= QTableWidgetItem(str(rs_nota[10]))
        parcial_b3= QTableWidgetItem(str(rs_nota[11]))
        parcial_b4= QTableWidgetItem(str(rs_nota[12]))
        prom1=(str(round(int((rs_nota[1]+rs_nota[5]+rs_nota[9])/3))))
        prom2=(str(round(int((rs_nota[2]+rs_nota[6]+rs_nota[10])/3))))
        prom3=(str(round(int((rs_nota[3]+rs_nota[7]+rs_nota[11])/3))))
        prom4=(str(round(int((rs_nota[4]+rs_nota[8]+rs_nota[12])/3))))
        entrar.tableWidget_3.setItem(0,0,tarea_b1)
        entrar.tableWidget_3.setItem(0,1,tarea_b2)
        entrar.tableWidget_3.setItem(0,2,tarea_b3)
        entrar.tableWidget_3.setItem(0,3,tarea_b4)
        entrar.tableWidget_3.setItem(1,0,parcial_b1)
        entrar.tableWidget_3.setItem(1,1,parcial_b2)
        entrar.tableWidget_3.setItem(1,2,parcial_b3)
        entrar.tableWidget_3.setItem(1,3,parcial_b4)
        entrar.tableWidget_3.setItem(2,0,bimestre1)
        entrar.tableWidget_3.setItem(2,1,bimestre2)
        entrar.tableWidget_3.setItem(2,2,bimestre3)
        entrar.tableWidget_3.setItem(2,3,bimestre4)
        entrar.tableWidget_3.setItem(2,3,bimestre4)
        entrar.tableWidget_3.setItem(2,3,bimestre4)
        entrar.tableWidget_3.setItem(2,3,bimestre4)
        entrar.tableWidget_3.setItem(2,3,bimestre4)
        entrar.tableWidget_3.setItem(2,3,bimestre4)
        entrar.tableWidget_3.setItem(3,0,QTableWidgetItem(prom1))
        entrar.tableWidget_3.setItem(3,1,QTableWidgetItem(prom2))
        entrar.tableWidget_3.setItem(3,2,QTableWidgetItem(prom3))
        entrar.tableWidget_3.setItem(3,3,QTableWidgetItem(prom4))
        entrar.tableWidget_3.setItem(3,4,QTableWidgetItem(str(round((int(prom1)+int(prom2)+int(prom3)+int(prom4))/4))))
        row+=1
def mostrar_nota_ed(rs_nota):
    row=0
    while(row<4):
        tarea_b1=QTableWidgetItem(str(rs_nota[1]))
        tarea_b2=QTableWidgetItem(str(rs_nota[2]))
        tarea_b3= QTableWidgetItem(str(rs_nota[3]))
        tarea_b4= QTableWidgetItem(str(rs_nota[4]))
        bimestre1= QTableWidgetItem(str(rs_nota[5]))
        bimestre2= QTableWidgetItem(str(rs_nota[6]))
        bimestre3= QTableWidgetItem(str(rs_nota[7]))
        bimestre4= QTableWidgetItem(str(rs_nota[8]))
        parcial_b1= QTableWidgetItem(str(rs_nota[9]))
        parcial_b2= QTableWidgetItem(str(rs_nota[10]))
        parcial_b3= QTableWidgetItem(str(rs_nota[11]))
        parcial_b4= QTableWidgetItem(str(rs_nota[12]))
        prom1=(str(round(int((rs_nota[1]+rs_nota[5]+rs_nota[9])/3))))
        prom2=(str(round(int((rs_nota[2]+rs_nota[6]+rs_nota[10])/3))))
        prom3=(str(round(int((rs_nota[3]+rs_nota[7]+rs_nota[11])/3))))
        prom4=(str(round(int((rs_nota[4]+rs_nota[8]+rs_nota[12])/3))))
        entrar.tableWidget_6.setItem(0,0,tarea_b1)
        entrar.tableWidget_6.setItem(0,1,tarea_b2)
        entrar.tableWidget_6.setItem(0,2,tarea_b3)
        entrar.tableWidget_6.setItem(0,3,tarea_b4)
        entrar.tableWidget_6.setItem(1,0,parcial_b1)
        entrar.tableWidget_6.setItem(1,1,parcial_b2)
        entrar.tableWidget_6.setItem(1,2,parcial_b3)
        entrar.tableWidget_6.setItem(1,3,parcial_b4)
        entrar.tableWidget_6.setItem(2,0,bimestre1)
        entrar.tableWidget_6.setItem(2,1,bimestre2)
        entrar.tableWidget_6.setItem(2,2,bimestre3)
        entrar.tableWidget_6.setItem(2,3,bimestre4)
        entrar.tableWidget_6.setItem(2,3,bimestre4)
        entrar.tableWidget_6.setItem(2,3,bimestre4)
        entrar.tableWidget_6.setItem(2,3,bimestre4)
        entrar.tableWidget_6.setItem(2,3,bimestre4)
        entrar.tableWidget_6.setItem(2,3,bimestre4)
        entrar.tableWidget_6.setItem(3,0,QTableWidgetItem(prom1))
        entrar.tableWidget_6.setItem(3,1,QTableWidgetItem(prom2))
        entrar.tableWidget_6.setItem(3,2,QTableWidgetItem(prom3))
        entrar.tableWidget_6.setItem(3,3,QTableWidgetItem(prom4))
        entrar.tableWidget_6.setItem(3,4,QTableWidgetItem(str(round((int(prom1)+int(prom2)+int(prom3)+int(prom4))/4))))
        row+=1
def mostrar_nota_tuto(rs_nota):
    row=0
    while(row<4):
        tarea_b1=QTableWidgetItem(str(rs_nota[1]))
        tarea_b2=QTableWidgetItem(str(rs_nota[2]))
        tarea_b3= QTableWidgetItem(str(rs_nota[3]))
        tarea_b4= QTableWidgetItem(str(rs_nota[4]))
        bimestre1= QTableWidgetItem(str(rs_nota[5]))
        bimestre2= QTableWidgetItem(str(rs_nota[6]))
        bimestre3= QTableWidgetItem(str(rs_nota[7]))
        bimestre4= QTableWidgetItem(str(rs_nota[8]))
        parcial_b1= QTableWidgetItem(str(rs_nota[9]))
        parcial_b2= QTableWidgetItem(str(rs_nota[10]))
        parcial_b3= QTableWidgetItem(str(rs_nota[11]))
        parcial_b4= QTableWidgetItem(str(rs_nota[12]))
        prom1=(str(round(int((rs_nota[1]+rs_nota[5]+rs_nota[9])/3))))
        prom2=(str(round(int((rs_nota[2]+rs_nota[6]+rs_nota[10])/3))))
        prom3=(str(round(int((rs_nota[3]+rs_nota[7]+rs_nota[11])/3))))
        prom4=(str(round(int((rs_nota[4]+rs_nota[8]+rs_nota[12])/3))))
        entrar.tableWidget_7.setItem(0,0,tarea_b1)
        entrar.tableWidget_7.setItem(0,1,tarea_b2)
        entrar.tableWidget_7.setItem(0,2,tarea_b3)
        entrar.tableWidget_7.setItem(0,3,tarea_b4)
        entrar.tableWidget_7.setItem(1,0,parcial_b1)
        entrar.tableWidget_7.setItem(1,1,parcial_b2)
        entrar.tableWidget_7.setItem(1,2,parcial_b3)
        entrar.tableWidget_7.setItem(1,3,parcial_b4)
        entrar.tableWidget_7.setItem(2,0,bimestre1)
        entrar.tableWidget_7.setItem(2,1,bimestre2)
        entrar.tableWidget_7.setItem(2,2,bimestre3)
        entrar.tableWidget_7.setItem(2,3,bimestre4)
        entrar.tableWidget_7.setItem(2,3,bimestre4)
        entrar.tableWidget_7.setItem(2,3,bimestre4)
        entrar.tableWidget_7.setItem(2,3,bimestre4)
        entrar.tableWidget_7.setItem(2,3,bimestre4)
        entrar.tableWidget_7.setItem(2,3,bimestre4)
        entrar.tableWidget_7.setItem(3,0,QTableWidgetItem(prom1))
        entrar.tableWidget_7.setItem(3,1,QTableWidgetItem(prom2))
        entrar.tableWidget_7.setItem(3,2,QTableWidgetItem(prom3))
        entrar.tableWidget_7.setItem(3,3,QTableWidgetItem(prom4))
        entrar.tableWidget_7.setItem(3,4,QTableWidgetItem(str(round((int(prom1)+int(prom2)+int(prom3)+int(prom4))/4))))
        row+=1
def mostrar_nota_comu(rs_nota):
    row=0
    while(row<4):
        tarea_b1=QTableWidgetItem(str(rs_nota[1]))
        tarea_b2=QTableWidgetItem(str(rs_nota[2]))
        tarea_b3= QTableWidgetItem(str(rs_nota[3]))
        tarea_b4= QTableWidgetItem(str(rs_nota[4]))
        bimestre1= QTableWidgetItem(str(rs_nota[5]))
        bimestre2= QTableWidgetItem(str(rs_nota[6]))
        bimestre3= QTableWidgetItem(str(rs_nota[7]))
        bimestre4= QTableWidgetItem(str(rs_nota[8]))
        parcial_b1= QTableWidgetItem(str(rs_nota[9]))
        parcial_b2= QTableWidgetItem(str(rs_nota[10]))
        parcial_b3= QTableWidgetItem(str(rs_nota[11]))
        parcial_b4= QTableWidgetItem(str(rs_nota[12]))
        prom1=(str(round(int((rs_nota[1]+rs_nota[5]+rs_nota[9])/3))))
        prom2=(str(round(int((rs_nota[2]+rs_nota[6]+rs_nota[10])/3))))
        prom3=(str(round(int((rs_nota[3]+rs_nota[7]+rs_nota[11])/3))))
        prom4=(str(round(int((rs_nota[4]+rs_nota[8]+rs_nota[12])/3))))
        entrar.tableWidget_5.setItem(0,0,tarea_b1)
        entrar.tableWidget_5.setItem(0,1,tarea_b2)
        entrar.tableWidget_5.setItem(0,2,tarea_b3)
        entrar.tableWidget_5.setItem(0,3,tarea_b4)
        entrar.tableWidget_5.setItem(1,0,parcial_b1)
        entrar.tableWidget_5.setItem(1,1,parcial_b2)
        entrar.tableWidget_5.setItem(1,2,parcial_b3)
        entrar.tableWidget_5.setItem(1,3,parcial_b4)
        entrar.tableWidget_5.setItem(2,0,bimestre1)
        entrar.tableWidget_5.setItem(2,1,bimestre2)
        entrar.tableWidget_5.setItem(2,2,bimestre3)
        entrar.tableWidget_5.setItem(2,3,bimestre4)
        entrar.tableWidget_5.setItem(2,3,bimestre4)
        entrar.tableWidget_5.setItem(2,3,bimestre4)
        entrar.tableWidget_5.setItem(2,3,bimestre4)
        entrar.tableWidget_5.setItem(2,3,bimestre4)
        entrar.tableWidget_5.setItem(2,3,bimestre4)
        entrar.tableWidget_5.setItem(3,0,QTableWidgetItem(prom1))
        entrar.tableWidget_5.setItem(3,1,QTableWidgetItem(prom2))
        entrar.tableWidget_5.setItem(3,2,QTableWidgetItem(prom3))
        entrar.tableWidget_5.setItem(3,3,QTableWidgetItem(prom4))
        entrar.tableWidget_5.setItem(3,4,QTableWidgetItem(str(round((int(prom1)+int(prom2)+int(prom3)+int(prom4))/4))))
        row+=1
def mostrar_nota_cien(rs_nota):
    row=0
    while(row<4):
        tarea_b1=QTableWidgetItem(str(rs_nota[1]))
        tarea_b2=QTableWidgetItem(str(rs_nota[2]))
        tarea_b3= QTableWidgetItem(str(rs_nota[3]))
        tarea_b4= QTableWidgetItem(str(rs_nota[4]))
        bimestre1= QTableWidgetItem(str(rs_nota[5]))
        bimestre2= QTableWidgetItem(str(rs_nota[6]))
        bimestre3= QTableWidgetItem(str(rs_nota[7]))
        bimestre4= QTableWidgetItem(str(rs_nota[8]))
        parcial_b1= QTableWidgetItem(str(rs_nota[9]))
        parcial_b2= QTableWidgetItem(str(rs_nota[10]))
        parcial_b3= QTableWidgetItem(str(rs_nota[11]))
        parcial_b4= QTableWidgetItem(str(rs_nota[12]))
        prom1=(str(round(int((rs_nota[1]+rs_nota[5]+rs_nota[9])/3))))
        prom2=(str(round(int((rs_nota[2]+rs_nota[6]+rs_nota[10])/3))))
        prom3=(str(round(int((rs_nota[3]+rs_nota[7]+rs_nota[11])/3))))
        prom4=(str(round(int((rs_nota[4]+rs_nota[8]+rs_nota[12])/3))))
        entrar.tableWidget_4.setItem(0,0,tarea_b1)
        entrar.tableWidget_4.setItem(0,1,tarea_b2)
        entrar.tableWidget_4.setItem(0,2,tarea_b3)
        entrar.tableWidget_4.setItem(0,3,tarea_b4)
        entrar.tableWidget_4.setItem(1,0,parcial_b1)
        entrar.tableWidget_4.setItem(1,1,parcial_b2)
        entrar.tableWidget_4.setItem(1,2,parcial_b3)
        entrar.tableWidget_4.setItem(1,3,parcial_b4)
        entrar.tableWidget_4.setItem(2,0,bimestre1)
        entrar.tableWidget_4.setItem(2,1,bimestre2)
        entrar.tableWidget_4.setItem(2,2,bimestre3)
        entrar.tableWidget_4.setItem(2,3,bimestre4)
        entrar.tableWidget_4.setItem(2,3,bimestre4)
        entrar.tableWidget_4.setItem(2,3,bimestre4)
        entrar.tableWidget_4.setItem(2,3,bimestre4)
        entrar.tableWidget_4.setItem(2,3,bimestre4)
        entrar.tableWidget_4.setItem(2,3,bimestre4)
        entrar.tableWidget_4.setItem(3,0,QTableWidgetItem(prom1))
        entrar.tableWidget_4.setItem(3,1,QTableWidgetItem(prom2))
        entrar.tableWidget_4.setItem(3,2,QTableWidgetItem(prom3))
        entrar.tableWidget_4.setItem(3,3,QTableWidgetItem(prom4))
        entrar.tableWidget_4.setItem(3,4,QTableWidgetItem(str(round((int(prom1)+int(prom2)+int(prom3)+int(prom4))/4))))
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
entrar.pushButton_5.clicked.connect(cerrar_sesion)


entrar_tutor.pushButton_5.clicked.connect(cerrar_sesion)

login.show()
app.exec_()
