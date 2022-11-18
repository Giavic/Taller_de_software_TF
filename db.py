import pymysql as sql
from random import *
import datetime

class Database:
    def __init__(self):
        self.connection = sql.connect(host='remotemysql.com',user='kSWJ1SMJwX',password='2HblF4zbnB',database='kSWJ1SMJwX')
        self.cursor = self.connection.cursor()
        print("Conectado")

    def registro_alumno(self, nombre, apellido, correo, contraseña,aula):
        id=randint(1, 1000000)
        self.cursor.execute('INSERT INTO Alumno VALUES ({0}, "{1}", "{2}", "{3}", "{4}","{5}")'.format(id,nombre, apellido, correo, contraseña, aula))
        id_curso1=randint(1, 100000000)
        id_curso2=randint(1, 100000000)
        id_curso3=randint(1, 100000000)
        id_curso4=randint(1, 100000000)
        id_curso5=randint(1, 100000000)
        self.cursor.execute('INSERT INTO Nota VALUES ({0},0,0,0,0,0,0,0,0,0,0,0,0,{1},"Matemática")'.format(id_curso1,id))
        self.cursor.execute('INSERT INTO Nota VALUES ({0},0,0,0,0,0,0,0,0,0,0,0,0,{1},"Ciencias")'.format(id_curso2,id))
        self.cursor.execute('INSERT INTO Nota VALUES ({0},0,0,0,0,0,0,0,0,0,0,0,0,{1},"Comunicación")'.format(id_curso3,id))
        self.cursor.execute('INSERT INTO Nota VALUES ({0},0,0,0,0,0,0,0,0,0,0,0,0,{1},"Educación Física")'.format(id_curso4,id))
        self.cursor.execute('INSERT INTO Nota VALUES ({0},0,0,0,0,0,0,0,0,0,0,0,0,{1},"Tutoría")'.format(id_curso5,id))
        self.connection.commit()

    def registro_tutor(self, nombre, apellido,aula, correo, contraseña):
        id=randint(1, 1000000)
        self.cursor.execute('INSERT INTO Tutor VALUES ({0}, "{1}", "{2}", "{3}", "{4}","{5}")'.format(id,nombre, apellido,aula, correo, contraseña))
        self.connection.commit()

    def login_alumno(self, correo, password):
        self.cursor.execute('SELECT * FROM Alumno WHERE correo = "{0}" AND contraseña = "{1}"'.format(correo, password))
        return self.cursor.fetchone()

    def login_tutor(self, correo, password):
        self.cursor.execute('SELECT * FROM Tutor WHERE correo = "{0}" AND contraseña = "{1}"'.format(correo, password))
        return self.cursor.fetchone()

    def registro_reporte(self,comentario,fecha,id_alumno):
        id=randint(1, 1000000)
        now=datetime.datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute('INSERT INTO Reporte VALUES ({0}, "{1}", "{2}", {3})'.format(id,comentario,fecha,id_alumno))
        self.connection.commit()
    
    def mostrar_reportes(self,id):
        self.cursor.execute('SELECT * FROM Reporte WHERE id_alumno = {0}'.format(id))
        return self.cursor.fetchall()

    def mostrar_notas(self,id,curso):
        self.cursor.execute('SELECT * FROM Nota WHERE id_alumno = {0} and curso="{1}" '.format(id,curso))
        return self.cursor.fetchone()

    def mostrar_alumnos(self,aula):
        self.cursor.execute('SELECT * FROM Alumno WHERE aula = "{0}"'.format(aula))
        return self.cursor.fetchall()
    
    def buscar_alumno(self,nombre,apellido):
        self.cursor.execute('SELECT * FROM Alumno WHERE nombre = "{0}" and apellido="{1}"'.format(nombre,apellido))
        return self.cursor.fetchone()

    def registrar_nota(self,b1,b2,b3,b4,p1,p2,p3,p4,t1,t2,t3,t4,id_alumno,curso):
        self.cursor.execute('UPDATE Nota SET nota_b1={0},nota_b2={1},nota_b3={2},nota_b4={3},nota_p1={4},nota_p2={5},nota_p3={6},nota_p4={7},nota_t1={8},nota_t2={9},nota_t3={10},nota_t4={11} WHERE id_alumno={12} and curso="{13}"'.format(b1,b2,b3,b4,p1,p2,p3,p4,t1,t2,t3,t4,id_alumno,curso))
        self.connection.commit()
    
    def notas_reporte(self,id_alumno):
        self.cursor.execute('SELECT * FROM Nota WHERE id_alumno = {0}'.format(id_alumno))
        return self.cursor.fetchall()

    def mostrar_reportes_tutor(self,aula):
        self.cursor.execute('SELECT Alumno.nombre,Alumno.apellido,Reporte.comentario,Reporte.fecha FROM Reporte INNER JOIN Alumno ON Reporte.id_alumno=Alumno.id WHERE Alumno.aula = "{0}"'.format(aula))
        return self.cursor.fetchall()
    
    def registrar_evento(self,evento,fecha,aula):
        id=randint(1, 1000000)
        self.cursor.execute('INSERT INTO Eventos VALUES ({0}, "{1}", "{2}", "{3}")'.format(id,evento,fecha,aula))
        self.connection.commit()

    def mostrar_eventos(self,aula,fecha):
        self.cursor.execute('SELECT * FROM Eventos WHERE aula = "{0}" and fecha="{1}"'.format(aula,fecha))
        return self.cursor.fetchall()
