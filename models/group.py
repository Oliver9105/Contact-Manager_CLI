# models/group.py
from database import Database

class Group:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_table(cls):
        db = Database()
        db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        db.conn.commit()
