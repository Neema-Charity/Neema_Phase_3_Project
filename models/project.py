from models.conn import conn, c

class Project:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    @staticmethod
    def create_table():
        c.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            material TEXT NOT NULL
        )""")
        conn.commit()

    def add_project(self):
        c.execute("INSERT INTO projects (name, material) VALUES (?,?)", (self.name, self.material))
        conn.commit()

    @staticmethod
    def update_project(id, name, material):
        c.execute("UPDATE projects SET name =?, material =? WHERE id =?", (name, material, id))
        conn.commit()

    @staticmethod
    def get_projects():
        c.execute("SELECT * FROM projects")
        return c.fetchall()

    @staticmethod
    def get_project(id):
        c.execute("SELECT * FROM projects WHERE id =?", (id,))
        return c.fetchone()

    @staticmethod
    def remove_project(id):
        c.execute("DELETE FROM projects WHERE id =?", (id,))
        conn.commit()
