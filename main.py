from config.connection import Connection
from models.autor import Autor
from models.editorial import Editorial
from models.lector import Lector
from models.libro import Libros
from models.prestamos import Prestamos


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
                self.view_autores()
            elif opcion == "3":
                self.view_editoriales()
            elif opcion =="4":
                self.view_libros()
            elif opcion == "5":
                self.view_prestamos()
            if opcion =="5":
                pass
            else:
                self.salir()

#Lector

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
                self.data_update_lector()
            elif opcion == "4":
                self.data_delete_lector()
            elif opcion == "5":
                self.view_principal()
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

    def choose_lector(self):
        Lector.all_lectores("xx")
        print('''ESCOGER ID DE ALUMNOS:''')

    def data_update_lector(self):
        self.choose_lector()
        id = input("> ")

        print(''' INGRESAR DATOS DEL LECTOR:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")
        print(''' DNI: ''')
        dni = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        print(''' CELULAR: ''')
        celular = input("> ")
        print(''' DOMICILIO: ''')
        domicilio = input("> ")

        update = Lector(id, nombre, dni, correo, celular, domicilio)
        update.update_lector()

    def data_delete_lector(self):
        self.choose_lector()
        id = input("> ")

        delete = Lector(id)
        delete.delete_lector()

#Autores

    def view_autores(self):
        while True:
            print('''
                Escoga una opción:
                1) Registrar nuevo autor
                2) Lista de autores
                3) Modificar autor
                4) Eliminar autor
                5) Regresar
                6) Salir\n
            ''')
            opcion = input(">")
            if opcion == "1":
                self.data_insert_autor()
            elif opcion == "2":
                Autor.all_autores("xx")
            elif opcion == "3":
                self.data_update_autor()
            elif opcion == "4":
                self.data_delete_autor()
            elif opcion == "5":
                self.view_principal()
            else:
                self.salir()

    def data_insert_autor(self):
        print(''' INGRESAR DATOS DEL AUTOR:''')
        print(''' NOMBRE: ''')
        nombre = input("> ")

        insert = Autor('', nombre)
        insert.insert_autor()   

    def choose_autor(self):
        Autor.all_autores("xx")
        print('''ESCOGER ID DEL AUTOR:''')

    def data_update_autor(self):
        self.choose_autor()
        id = input("> ")

        print(''' INGRESAR DATOS DEL AUTOR:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")

        update = Autor(id, nombre)
        update.update_autor()

    def data_delete_autor(self):
        self.choose_autor()
        id = input("> ")

        delete = Autor(id,"")
        delete.delete_autor()

#Editoriales
    def view_editoriales(self):
        while True:
            print('''
                Escoga una opción:
                1) Registrar nueva editorial
                2) Lista de editoriales
                3) Modificar editorial
                4) Eliminar editorial
                5) Regresar
                6) Salir\n
            ''')
            opcion = input(">")
            if opcion == "1":
                self.data_insert_editorial()
            elif opcion == "2":
                Editorial.all_editoriales("xx")
            elif opcion == "3":
                self.data_update_editorial()
            elif opcion == "4":
                self.data_delete_editorial()
            elif opcion == "5":
                self.view_principal()
            else:
                self.salir()

    def data_insert_editorial(self):
        print(''' INGRESAR DATOS DE LA EDITORIAL:''')
        print(''' NOMBRE: ''')
        nombre = input("> ")

        insert = Editorial('', nombre)
        insert.insert_editorial()   

    def choose_editorial(self):
        Editorial.all_editoriales("xx")
        print('''ESCOGER ID DE LA EDITORIAL:''')

    def data_update_editorial(self):
        self.choose_editorial()
        id = input("> ")

        print(''' INGRESAR DATOS DE LA EDITORIAL:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")

        update = Editorial(id, nombre)
        update.update_editorial()

    def data_delete_editorial(self):
        self.choose_editorial()
        id = input("> ")

        delete = Editorial(id,"")
        delete.delete_editorial()

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

# Prestamos

    def view_prestamos(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo
                2) Modificar Prestamo
                3) Eliminar Prestamo
                4) Devoluciones
                5) Regresar
                6) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.add_prestamos()
            elif opcion == "2":
                self.data_update_prestamos()
            elif opcion == "3":
                self.data_delete_prestamos()
            elif opcion == "5":
                self.view_principal()
            elif opcion == '4':
                self.data_devoluciones()
            else:
                self.salir()

    def choose_prestamos(self):
        Prestamos.all_prestamos("xx")
        print('''ESCOGER ID DEL LIBRO:''')
    
    def add_prestamos(self):
        print(''' INGRESAR LECTOR ID:''')
        lector_id = input("> ")
        print(''' INGRESAR LIBRO ID:''')
        libro_id = input("> ")
        print(''' INGRESAR FECHAINICIAL:''')
        fechainicial = input("> ")
        print(''' INGRESAR DIAS PRESTAMOS:''')
        dias_prestamo = input("> ")
        print(''' INGRESAR FECHA DEV PROGRAMADA:''')
        fechadev_prog = input("> ")
        
        insert = Prestamos('', lector_id, libro_id, fechainicial, dias_prestamo, fechadev_prog, '1900-01-01')
        insert.insert_prestamos()

        update = Prestamos(libro_id, '', '', '', '', '', '', '0')
        update.update_state_libro()

    def data_update_prestamos(self):
        self.choose_prestamos()
        id = input("> ")

        print(''' INGRESAR LECTOR ID:''')
        lector_id = input("> ")
        print(''' INGRESAR LIBRO ID:''')
        libro_id = input("> ")
        print(''' INGRESAR FECHAINICIAL:''')
        fechainicial = input("> ")
        print(''' INGRESAR DIAS PRESTAMOS:''')
        dias_prestamo = input("> ")
        print(''' INGRESAR FECHA DEV PROGRAMADA:''')
        fechadev_prog = input("> ")
        print(''' INGRESAR FECHA DEV REAL:''')
        fechadev_real = input("> ")

        update = Prestamos(id, lector_id, libro_id, fechainicial, dias_prestamo, fechadev_prog, fechadev_real)
        update.update_prestamos()

    def data_delete_prestamos(self):
        self.choose_prestamos()
        id = input("> ")
        
        delete = Prestamos(id, '', '', '', '', '', '')
        delete.delete_prestamos()

    def data_devoluciones(self):
        self.choose_prestamos()
        id = input("> ")

        print(''' INGRESAR FECHA ENTREGA REAL:''')
        fechadev_real = input("> ")

        update = Prestamos(id, fechadev_real)
        update.update_prestamos()

        update = Prestamos(id, '', '', '', '', '', '', '1')
        update.update_state_libro()

    def salir(self):
        print('*** SISTEMA CERRADO ***')
        exit()


Biblioteca()