from models.conn import conn, c

class Material:
    def __init__(self, name, quantity, supplier, project):
        self.name = name
        self.quantity = quantity
        self.supplier = supplier
        self.project = project

    @staticmethod
    def create_table():
        c.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            supplier TEXT NOT NULL,
            project TEXT NOT NULL
        )""")
        conn.commit()

    def add_material(self):
        c.execute("INSERT INTO materials (name, quantity, supplier, project) VALUES (?,?,?,?)", (self.name, self.quantity, self.supplier, self.project))
        conn.commit()

    @staticmethod
    def update_material(id, name, quantity, supplier, project):
        c.execute("UPDATE materials SET name =?, quantity =?, supplier =?, project =? WHERE id =?", (name, quantity, supplier, project, id))
        conn.commit()

    @staticmethod
    def get_materials():
        c.execute("SELECT * FROM materials")
        return c.fetchall()

    @staticmethod
    def get_material(id):
        c.execute("SELECT * FROM materials WHERE id =?", (id,))
        return c.fetchone()

    @staticmethod
    def remove_material(id):
        c.execute("DELETE FROM materials WHERE id =?", (id,))
        conn.commit()
