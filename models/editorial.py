from helpers import *

class Editorial:
    def __init__(self, id, nombre):
        self.create_table()
        self.id = id
        self.nombre = nombre
        

    def create_table(self):
        try:
            conn = Connection('editorial')
            query = '''
                CREATE TABLE IF NOT EXISTS editorial(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(35) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_editoriales(self):
        try:
            conn = Connection('editorial')
            records = conn.select([])
            
            for record in records:
                print(f'{record[0]}: {record[1]}')
        except Exception as e:
            print(e)

    def insert_editorial(self):
        try:
            conn = Connection('editorial')
            conn.insert({
                'nombre': self.nombre
            })
            print(f'Se registro la editorial: {self.nombre}')
        except Exception as e:
            print(e)

    def update_editorial(self):
        try:
            conn = Connection('editorial')
            conn.update({
                'id' : self.id
            },{
                'nombre': self.nombre,
            })
            print(f'Se modifico el editorial: {self.nombre}')
        except Exception as e:
            print(e)
        
    def delete_editorial(self):
        try:
            conn = Connection('editorial')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el editorial.')
        except Exception as e:
            print(e)