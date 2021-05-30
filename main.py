
from config.connection import Connection
from models.autor import Autor
from models.editorial import Editorial
from models.lector import Lector
from models.libro import Libros

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
            if opcion =="4":
                self.view_libros()
            if opcion =="5":
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

# Libros

    def view_libros(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo
                2) Modificar Libro
                3) Eliminar Libro
                4) Regresar
                5) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.add_libros()
            elif opcion == "2":
                self.data_update_libros()
            elif opcion == "3":
                self.data_delete_libros()
            elif opcion == "4":
                self.view_principal()
            else:
                self.salir()

    def choose_libros(self):
        Libros.all_libros("xx")
        print('''ESCOGER ID DEL LIBRO:''')
    
    def add_libros(self):
        print(''' INGRESAR CODIGO:''')
        codigo = input("> ")
        print(''' INGRESAR TITULO:''')
        titulo = input("> ")
        print(''' INGRESAR ID AUTOR:''')
        autor_id = input("> ")
        print(''' INGRESAR ID EDITORIAL:''')
        editorial_id = input("> ")
        
        insert = Libros('', codigo, titulo, autor_id, editorial_id, '1')
        insert.insert_libros()

    def data_libros_profesor(self):
        self.choose_profesor()
        profesor_id = input("> ")
        self.choose_salon()
        salon_id = input("> ")
        self.choose_libros()
        curso_id = input("> ")

        insert = Salon(profesor_id, salon_id, curso_id)
        insert.insert_salon()


    def data_update_libros(self):
        self.choose_libros()
        id = input("> ")

        print(''' INGRESAR CODIGO:''')
        codigo = input("> ")
        print(''' INGRESAR TITULO:''')
        titulo = input("> ")
        print(''' INGRESAR ID AUTOR:''')
        autor_id = input("> ")
        print(''' INGRESAR ID EDITORIAL:''')
        editorial_id = input("> ")
        print(''' INGRESAR ESTADO 1/0:''')
        estado = input("> ")

        update = Libros(id, codigo, titulo, autor_id, editorial_id, estado)
        update.update_libros()

    def data_delete_libros(self):
        self.choose_libros()
        id = input("> ")
        
        delete = Libros(id, '', '', '', '', '')
        delete.delete_libros()


    def salir(self):
        print('*** SISTEMA CERRADO ***')
        exit()

Biblioteca()