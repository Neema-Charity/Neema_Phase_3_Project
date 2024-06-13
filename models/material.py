from models.base import BaseModel

class Material(BaseModel):
    def __init__(self, name, quantity, supplier_id, project_id=None):
        self.name = name
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.project_id = project_id

    @classmethod
    def create_table(cls):
        query = '''
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            supplier_id INTEGER,
            project_id INTEGER,
            UNIQUE(name),
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
            FOREIGN KEY (project_id) REFERENCES projects(id)
        )
        '''
        cls.execute_query(query)

    def add_material(self):
        query = '''
        INSERT INTO materials (name, quantity, supplier_id, project_id)
        VALUES (?, ?, ?, ?)
        '''
        self.execute_query(query, (self.name, self.quantity, self.supplier_id, self.project_id))

    @classmethod
    def get_materials(cls):
        query = 'SELECT * FROM materials'
        return cls.fetch_all(query)

    @classmethod
    def get_material(cls, id):
        query = 'SELECT * FROM materials WHERE id = ?'
        return cls.fetch_one(query, (id,))

    @classmethod
    def update_material(cls, id, name, quantity, supplier_id, project_id):
        query = '''
        UPDATE materials
        SET name = ?, quantity = ?, supplier_id = ?, project_id = ?
        WHERE id = ?
        '''
        cls.execute_query(query, (name, quantity, supplier_id, project_id, id))

    @classmethod
    def remove_material(cls, id):
        query = 'DELETE FROM materials WHERE id = ?'
        cls.execute_query(query, (id,))
