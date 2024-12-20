# models/contact_group.py
from database import Database

class ContactGroup:
    @classmethod
    def create_table(cls):
        db = Database()
        db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contact_group (
                contact_id INTEGER,
                group_id INTEGER,
                FOREIGN KEY (contact_id) REFERENCES contacts(id),
                FOREIGN KEY (group_id) REFERENCES groups(id),
                PRIMARY KEY (contact_id, group_id)
            )
        """)
        db.conn.commit()