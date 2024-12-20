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

    @classmethod
    def assign_contact_to_group(cls, contact_id, group_id):
        db = Database()
        db.cursor.execute("""
            INSERT INTO contact_group (contact_id, group_id)
            VALUES (?, ?)
        """, (contact_id, group_id))
        db.conn.commit()

    @classmethod
    def get_groups_for_contact(cls, contact_id):
        db = Database()
        db.cursor.execute("""
            SELECT g.name 
            FROM groups g
            JOIN contact_group cg ON g.id = cg.group_id 
            WHERE cg.contact_id = ?
        """, (contact_id,))
        return db.cursor.fetchall()

    @classmethod
    def get_contacts_for_group(cls, group_id):
        db = Database()
        db.cursor.execute("""
            SELECT c.name
            FROM contacts c
            JOIN contact_group cg ON c.id = cg.contact_id
            WHERE cg.group_id = ?
        """, (group_id,))
        return db.cursor.fetchall()

    @classmethod
    def remove_contact_from_group(cls, contact_id, group_id):
        db = Database()
        db.cursor.execute("""
            DELETE FROM contact_group WHERE contact_id = ? AND group_id = ?
        """, (contact_id, group_id))
        db.conn.commit()