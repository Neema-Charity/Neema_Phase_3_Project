import sqlite3
from contextlib import contextmanager

class BaseModel:
    db_path = 'construction.db'

    @classmethod
    @contextmanager
    def get_connection(cls):
        conn = sqlite3.connect(cls.db_path)
        try:
            yield conn
        finally:
            conn.close()

    @classmethod
    def execute_query(cls, query, params=()):
        with cls.get_connection() as conn:
            c = conn.cursor()
            c.execute(query, params)
            conn.commit()
            return c

    @classmethod
    def fetch_all(cls, query, params=()):
        with cls.get_connection() as conn:
            c = conn.cursor()
            c.execute(query, params)
            return c.fetchall()

    @classmethod
    def fetch_one(cls, query, params=()):
        with cls.get_connection() as conn:
            c = conn.cursor()
            c.execute(query, params)
            return c.fetchone()
