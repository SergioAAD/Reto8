from psycopg2 import connect

class Connection:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = connect(host='localhost', user='postgres', password='Toguman2412', 
                        database='Bibloteca', port=5432)
        self.cursor = self.db.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.commit()
    
    def select(self, data=[]): # lista
        fields = ", ".join(data)
        if not len(data): # False
            fields = '*'

        query = f'''
            SELECT {fields} FROM {self.table_name} ORDER BY id
        '''
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, data):
        list_values = ""
        for value in data.values():
            if isinstance(value, str):
                value = f"'{value}'"
            list_values += f'{value},'
        print(list_values)
        query = f'''
            INSERT INTO {self.table_name} ({", ".join(data.keys())}) VALUES ({list_values[:-1]})
        '''
        self.execute_query(query)
        return True

    def commit(self):
        self.db.commit()
        return True

    def rollback(self):
        self.db.rollback()
        return True      