from models.base import BaseModel

class Supplier(BaseModel):
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_table(cls):
        query = '''
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            UNIQUE(name)
        )
        '''
        cls.execute_query(query)

    def add_supplier(self):
        query = 'INSERT INTO suppliers (name) VALUES (?)'
        self.execute_query(query, (self.name,))

    @classmethod
    def get_suppliers(cls):
        query = 'SELECT * FROM suppliers'
        return cls.fetch_all(query)

    @classmethod
    def get_supplier(cls, id):
        query = 'SELECT * FROM suppliers WHERE id = ?'
        return cls.fetch_one(query, (id,))

    @classmethod
    def update_supplier(cls, id, name):
        query = 'UPDATE suppliers SET name = ? WHERE id = ?'
        cls.execute_query(query, (name, id))

    @classmethod
    def remove_supplier(cls, id):
        query = 'DELETE FROM suppliers WHERE id = ?'
        cls.execute_query(query, (id,))
