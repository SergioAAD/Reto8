
from config.connection import Connection
from models.autor import Autor
from models.editorial import Editorial
from models.lector import Lector

class Biblioteca():
    def __init__(self):
        self.view_principal()
    
    def view_principal(self):
        while True:
            print(''' *** BIENVENIDO AL GESTIOS DE BIBLIOTECA ***
            ¿Qué deseas realizar?
                1)Ver lectores
                2)Ver autores
                3)Ver editoriales
                4)Salir\n    
            ''')
            opcion = input(">")
            if opcion =="1":
                pass
            if opcion =="2":
                pass
            if opcion =="3":
                pass
            else:
                self.salir()


    def salir(self):
        print('*** SISTEMA CERRADO ***')
        exit()

Biblioteca()