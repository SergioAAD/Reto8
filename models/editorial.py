from helpers import *

class Editorial:
    def __init__(self, id):
        self.id = id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS editorial(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre_editorial character varying(35) NOT NULL
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