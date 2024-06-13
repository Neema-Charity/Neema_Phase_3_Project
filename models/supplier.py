from models.conn import conn, c

class Supplier:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    @staticmethod
    def create_table():
        c.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            material TEXT NOT NULL
        )""")
        conn.commit()

    def add_supplier(self):
        c.execute("INSERT INTO suppliers (name, material) VALUES (?,?)", (self.name, self.material))
        conn.commit()

    @staticmethod
    def update_supplier(id, name, material):
        c.execute("UPDATE suppliers SET name =?, material =? WHERE id =?", (name, material, id))
        conn.commit()

    @staticmethod
    def get_suppliers():
        c.execute("SELECT * FROM suppliers")
        return c.fetchall()

    @staticmethod
    def get_supplier(id):
        c.execute("SELECT * FROM suppliers WHERE id =?", (id,))
        return c.fetchone()

    @staticmethod
    def remove_supplier(id):
        c.execute("DELETE FROM suppliers WHERE id =?", (id,))
        conn.commit()
