from database import Database

class Contact:
    def __init__(self, name, phone_number, email): 
        self.name = name
        self.phone_number = phone_number
        self.email = email

    @classmethod
    def create_table(cls):
        db = Database()
        db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        db.conn.commit()

@classmethod
def get_groups_for_contact(cls, contact_id):
    db = Database()
    db.cursor.execute("""
        SELECT groups.name 
        FROM groups 
        JOIN contact_group ON groups.id = contact_group.group_id 
        WHERE contact_group.contact_id = ?
    """, (contact_id,))
    return db.cursor.fetchall()


@classmethod
def get_all_contacts(cls):
    db = Database()
    db.cursor.execute("SELECT * FROM contacts")
    return db.cursor.fetchall()
