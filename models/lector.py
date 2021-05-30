
from helpers import *

class Lector:
    def __init__(self, id="", nombre="", dni="", correo="", celular="", domicilio=""):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.correo = correo
        self.celular = celular
        self.domicilio = domicilio

    def create_table(self):
        try:
            conn = Connection()
            query = ''''
                CREATE TABLE IF NOT EXISTS lector(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre character varying(50) NOT NULL,
                    dni character varying(8) NOT NULL,
                    correo character varying(25) NOT NULL,
                    celular character varying(9) NOT NULL,
                    domicilio character varying(25) NOT NULL,
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_lectores(self):
        try:
            conn = Connection('lector')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE LECTORES --".center(80))
            p.field_names = ["ID", "Nombres", "DNI", "Correo", "Celular", "Domicilio"]

            for record in records:
                p.add_row([record[0], record[1], record[2], record[3], record[4], record[5]])
            print(p)
        except Exception as e:
            print(e)
        
    def insert_lector(self):
        try:
            conn = Connection('lector')
            conn.insert({
                'nombre': self.nombre,
                'dni': self.dni,
                'correo': self.correo,
                'celular': self.celular,
                'domicilio': self.domicilio
            })
            print(f'Se registro el lector: {self.nombre} con el dni {self.dni}, correo {self.correo}, celular {self.celular}, y domicilio {self.domicilio}')
        except Exception as e:
            print(e)    