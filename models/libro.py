from helpers import *

class Libros:
    def __init__(self, id, codigo, titulo, autor_id, editorial_id, estado):
        self.id = id
        self.codigo = codigo
        self.titulo = titulo
        self.autor_id = autor_id
        self.editorial_id = editorial_id
        self.estado = estado

        self.create_table()

    def create_table(self):
        try:
            conn = Connection('libro')
            query = '''
                CREATE TABLE IF NOT EXISTS libro(
                    id SERIAL PRIMARY KEY NOT NULL,
                    codigo character varying(35) NOT NULL,
                    titulo character varying(50) NOT NULL,
                    autor_id integer NOT NULL,
                    editorial_id integer NOT NULL,
                    estado integer NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_libros(self):
        try:
            conn = Connection('libro')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE libro --".center(80))
            p.field_names = ["ID", "Código", "Titulo", "Autor_id", "Editorial_id", "Estado"]

            for record in records:
                p.add_row([record[0], record[1], record[2], record[3], record[4], record[5]])
            print(p)
        except Exception as e:
            print(e)
    
    def list_all_libros(self):
        try:
            conn = Connection('libro')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE libro --".center(80))
            p.field_names = ["ID", "Nombres"]

            for record in records:
                p.add_row([record[0], record[1]])
            print(p)

        except Exception as e:
            print(e)

    def insert_libros(self):
        try:
            conn = Connection('libro')
            conn.insert({
                'codigo': self.codigo,
                'titulo': self.titulo,
                'autor_id': self.autor_id,
                'editorial_id': self.editorial_id,
                'estado': self.estado
            })
            print(f'Se registro el libro con el codigo {self.titulo}, titulo {self.codigo}, autor_id: {self.autor_id}, editorial_id {self.editorial_id}, estado {self.estado}')
        except Exception as e:
            print(e)

    def update_libros(self):
        try:
            conn = Connection('libro')
            conn.update({
                'id': self.id
            }, {
                'codigo': self.codigo,
                'titulo': self.titulo,
                'autor_id': self.autor_id,
                'editorial_id': self.editorial_id,
                'estado': self.estado
            })
            print(f'Se modifico el libro: {self.titulo}')
        except Exception as e:
            print(e)
    
    def delete_libros(self):
        try:
            conn = Connection('libro')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el libro.')
        except Exception as e:
            print(e)
