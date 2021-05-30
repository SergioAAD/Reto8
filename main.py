
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
                4)Ver libros
                5)Ver préstamos
                6)Salir\n    
            ''')
            opcion = input(">")
            if opcion == "1":
                self.view_lector()
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            else:
                self.salir()

    def view_lector(self):
        while True:
            print('''
                Escoga una opción:
                1) Registrar nuevo lector
                2) Lista de lectores
                3) Modificar lector
                4) Eliminar lector
                5) Regresar
                6) Salir\n
            ''')
            opcion = input(">")
            if opcion == "1":
                self.data_insert_lector()
            elif opcion == "2":
                Lector.all_lectores("xx")
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            else:
                self.salir()

    def data_insert_lector(self):
        print(''' INGRESAR DATOS DEL LECTOR:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")
        print(''' DNI: ''')
        dni = input("> ")
        print(''' CORREO: ''')
        celular = input("> ")
        print(''' CELULAR: ''')
        correo = input("> ")
        print(''' DOMICILIO: ''')
        domicilio = input("> ")

        insert = Lector('', nombre, dni, correo, celular, domicilio)
        insert.insert_lector()   

    def salir(self):
        print('*** SISTEMA CERRADO ***')
        exit()

Biblioteca()