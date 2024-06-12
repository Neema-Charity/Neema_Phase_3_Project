from models.conn import conn, c

class Supplier:
    def __init__(self, name, material, id):
        self.id = id
        self.name = name
        self.material = material

    def create_supplier(self, name, material):
        c.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            material TEXT NOT NULL
        )""")

    def add_supplier(self):
        c.execute("INSERT INTO suppliers (name, material) VALUES (?,?)", (self.name, self.material))
        conn.commit()

    def update_supplier(self, id, name, material):
        c.execute("UPDATE suppliers SET name =?, material =? WHERE id =?", (name, material, id))
        conn.commit()

    def get_suppliers(self):
        c.execute("SELECT * FROM suppliers")
        return c.fetchall()

    def get_supplier(self, id):
        c.execute("SELECT * FROM suppliers WHERE id =?", (id,))
        return c.fetchone()

    def remove_supplier(self, id):
        c.execute("DELETE FROM suppliers WHERE id =?", (id,))
        conn.commit()