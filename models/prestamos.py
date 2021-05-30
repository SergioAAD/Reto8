from helpers import *

class Prestamos:
    def __init__(self, id="", lector_id="", libro_id="", fechainicial="", dias_prestamo="", fechadev_prog="", fechadev_real="", estado=""):
        self.id = id
        self.lector_id = lector_id
        self.libro_id = libro_id
        self.fechainicial = fechainicial
        self.dias_prestamo = dias_prestamo
        self.fechadev_prog = fechadev_prog
        self.fechadev_real = fechadev_real
        self.estado = estado

        self.create_table()

    def create_table(self):
        try:
            conn = Connection('prestamo')
            query = '''
                CREATE TABLE IF NOT EXISTS prestamo(
                    id SERIAL PRIMARY KEY NOT NULL,
                    lector_id integer NOT NULL,
                    libro_id integer NOT NULL,
                    fechainicial date NOT NULL,
                    dias_prestamo integer NOT NULL,
                    fechadev_prog date NOT NULL,
                    fechadev_real date NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_prestamos(self):
        try:
            conn = Connection('prestamo')
            records = conn.select([])
            p = PrettyTable()
            print("-- LISTA DE PRESTAMOS --".center(80))
            p.field_names = ["ID", "Lector_id", "Libro_id", "fechainicial", "dias_prestamo", "fechadev_prog", "fechadev_real"]

            for record in records:
                p.add_row([record[0], record[1], record[2], record[3], record[4], record[5], record[6]])
            print(p)
        except Exception as e:
            print(e)
   
    def insert_prestamos(self):
        try:
            conn = Connection('prestamo')
            conn.insert({
                'lector_id': self.lector_id,
                'libro_id': self.libro_id,
                'fechainicial': self.fechainicial,
                'dias_prestamo': self.dias_prestamo,
                'fechadev_prog': self.fechadev_prog,
                'fechadev_real': self.fechadev_real
            })
            print(f'Se registro el prestamo con el lector_id {self.libro_id}, libro_id {self.lector_id}, fechainicial: {self.fechainicial}, dias_prestamo {self.dias_prestamo}, fechadev_prog {self.fechadev_prog}, fechadev_real {self.fechadev_real}')
        except Exception as e:
            print(e)

    def update_state_libro(self):
        try:
            conn = Connection('libro')
            conn.update({
                'id': self.id
            }, {
                'estado': self.estado
            })
            print(f'El libro ahora se encuentra NO Disponible')
        except Exception as e:
            print(e)
    
    def update_prestamos(self):
        try:
            conn = Connection('prestamo')
            conn.update({
                'id': self.id
            }, {
                'fechadev_real': self.lector_id
            })
            print(f'Se modifico el prestamo: {self.id}')
        except Exception as e:
            print(e)
    
    def delete_prestamos(self):
        try:
            conn = Connection('prestamo')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el prestamo.')
        except Exception as e:
            print(e)
