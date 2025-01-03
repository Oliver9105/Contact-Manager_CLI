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

    @classmethod
    def add_group(cls, name):
        db = Database()
        db.cursor.execute("""
            INSERT INTO groups (name)
            VALUES (?)
        """, (name,))
        db.conn.commit()

    @classmethod
    def get_all_groups(cls):
        db = Database()
        db.cursor.execute("SELECT * FROM groups")
        return db.cursor.fetchall()

    @classmethod
    def find_group_by_id(cls, group_id):
        db = Database()
        db.cursor.execute("SELECT * FROM groups WHERE id = ?", (group_id,))
        return db.cursor.fetchone()

    @classmethod
    def delete_group(cls, group_name):
        db = Database()
        db.cursor.execute("DELETE FROM groups WHERE name = ?", (group_name,))
        db.conn.commit()

