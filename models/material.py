from models.conn import conn, c

class Material:
    def __init__(self, name, quantity, supplier, project):
        self.name = name
        self.quantity = quantity
        self.supplier = supplier
        self.project = project

    def create_material(self, name, quantity, supplier, project):
        c.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            supplier TEXT NOT NULL,
            project TEXT NOT NULL
        )""")

    def add_material(self):
        c.execute("INSERT INTO materials (name, quantity, supplier, project) VALUES (?,?,?,?)", (self.name, self.quantity, self.supplier, self.project))
        conn.commit()

    def update_material(self, id, name, quantity, supplier, project):
        c.execute("UPDATE materials SET name =?, quantity =?, supplier =?, project =? WHERE id =?", (name, quantity, supplier, project, id))
        conn.commit()

    def get_materials(self):
        c.execute("SELECT * FROM materials")
        return c.fetchall()

    def get_material(self, id):
        c.execute("SELECT * FROM materials WHERE id =?", (id,))
        return c.fetchone()

    def remove_material(self, id):
        c.execute("DELETE FROM materials WHERE id =?", (id,))
        conn.commit()

