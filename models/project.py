from models.conn import conn, c

class Project:
    def __init__(self, project_name, material, id):
        self.id = id
        self.project_name = project_name
        self.material = material

    def create_project(self, name, material):
        c.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            material TEXT NOT NULL
        )""")

    def add_project(self):
        c.execute("INSERT INTO projects (name, material) VALUES (?,?)", (self.name, self.material))
        conn.commit()

    def update_project(self, id, name, material):
        c.execute("UPDATE projects SET name =?, material =? WHERE id =?", (name, material, id))
        conn.commit()

    def get_projects(self):
        c.execute("SELECT * FROM projects")
        return c.fetchall()

    def get_project(self, id):
        c.execute("SELECT * FROM projects WHERE id =?", (id,))
        return c.fetchone()

    def remove_project(self, id):
        c.execute("DELETE FROM projects WHERE id =?", (id,))
        conn.commit()

    
