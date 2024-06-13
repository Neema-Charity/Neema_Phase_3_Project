from models.base import BaseModel

class Project(BaseModel):
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_table(cls):
        query1 = '''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            UNIQUE(name)
        )
        '''
        query2 = '''
        CREATE TABLE IF NOT EXISTS project_materials (
            project_id INTEGER,
            material_id INTEGER,
            PRIMARY KEY (project_id, material_id),
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (material_id) REFERENCES materials(id)
        )
        '''
        cls.execute_query(query1)
        cls.execute_query(query2)

    def add_project(self):
        query = 'INSERT INTO projects (name) VALUES (?)'
        self.execute_query(query, (self.name,))

    @classmethod
    def get_projects(cls):
        query = 'SELECT * FROM projects'
        return cls.fetch_all(query)

    @classmethod
    def get_project(cls, id):
        query = 'SELECT * FROM projects WHERE id = ?'
        return cls.fetch_one(query, (id,))

    @classmethod
    def update_project(cls, id, name):
        query = 'UPDATE projects SET name = ? WHERE id = ?'
        cls.execute_query(query, (name, id))

    @classmethod
    def remove_project(cls, id):
        query1 = 'DELETE FROM projects WHERE id = ?'
        query2 = 'DELETE FROM project_materials WHERE project_id = ?'
        cls.execute_query(query2, (id,))
        cls.execute_query(query1, (id,))

    @classmethod
    def add_material_to_project(cls, project_id, material_id):
        query = 'INSERT INTO project_materials (project_id, material_id) VALUES (?, ?)'
        cls.execute_query(query, (project_id, material_id))

    @classmethod
    def get_materials_by_project(cls, project_id):
        query = '''
        SELECT m.* FROM materials m
        JOIN project_materials pm ON m.id = pm.material_id
        WHERE pm.project_id = ?
        '''
        return cls.fetch_all(query, (project_id,))
