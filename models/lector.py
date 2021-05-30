import prettytable
from helpers import *

class Lector:
    def __init__(self, id="", nombres="", dni="", correo="", celular="", domicilio=""):
        self.id = id
        self.nombres = nombres
        self.dni = dni
        self.correo = correo
        self.celular = celular
        self.domicilio = domicilio

    def create_table(self):
        try:
            conn = Connection()
            query = ''''
                    CREATE TABLE IF NOT EXIST lector(
                        id SERIAL PRIMARY KEY NOT NULL,
                        nombre character varying(50) NOT NULL,
                        dni character varying(8) NOT NULL
                        correo character varying(25) NOT NULL
                        celular character varying(9) NOT NULL
                        domicilio character varying(25) NOT NULL
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
            p = prettytable()
            print("-- LISTA DE LECTORES --".center(80))
            p.field_names = ["ID", "Nombres", "DNI", "Correo", "Domicilio"]

            for record in records:
                p.add_row([record[0], record[1], record[2], record[3], record[4], record[5], record[6]])
            print(p)
        except Exception as e:
            print(e)