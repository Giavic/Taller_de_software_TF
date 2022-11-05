import pymysql as sql
from random import *

class Database:
    def __init__(self):
        self.connection = sql.connect(host='remotemysql.com',user='kSWJ1SMJwX',password='2HblF4zbnB',database='kSWJ1SMJwX')
        self.cursor = self.connection.cursor()
        print("Conectado")

    def registro_alumno(self, nombre, apellido, correo, contraseña,aula):
        id=randint(1, 1000000)
        self.cursor.execute('INSERT INTO Alumno VALUES ({0}, "{1}", "{2}", "{3}", "{4}","{5}")'.format(id,nombre, apellido, correo, contraseña, aula))
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

    def registro_reporte(self,id,comentario,fecha,id_alumno):
        id=randint(1, 1000000)
        self.cursor.execute('INSERT INTO Reporte VALUES ({0}, "{1}", "{2}", "{3}")'.format(id,comentario,fecha,id_alumno))
        self.connection.commit()
    
    def mostrar_reportes(self,id):
        self.cursor.execute('SELECT * FROM Reporte WHERE id_alumno = {0}'.format(id))
        return self.cursor.fetchall()
    
