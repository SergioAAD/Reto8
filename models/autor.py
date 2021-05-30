from helpers import *

class Autor:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.create_table()

    def create_table(self):
        try:
            conn = Connection('autor')
            query = '''
                CREATE TABLE IF NOT EXISTS autor(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(35) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_autores(self):
        try:
            conn = Connection('autor')
            records = conn.select([])
            
            for record in records:
                print(f'{record[0]}: {record[1]}')
        except Exception as e:
            print(e)

    def insert_autor(self):
        try:
            conn = Connection('autor')
            conn.insert({
                'nombre': self.nombre
            })
            print(f'Se registro el lector: {self.nombre}')
        except Exception as e:
            print(e)

    def update_autor(self):
        try:
            conn = Connection('autor')
            conn.update({
                'id' : self.id
            },{
                'nombre': self.nombre,
            })
            print(f'Se modifico el editorial: {self.nombre}')
        except Exception as e:
            print(e)
        
    def delete_autor(self):
        try:
            conn = Connection('autor')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el autor.')
        except Exception as e:
            print(e)