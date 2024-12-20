from database import Database

class Contact:
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
    def add_contact(cls, name, phone_number, email):
        db = Database()
        db.cursor.execute("""
            INSERT INTO contacts (name, phone_number, email)
            VALUES (?, ?, ?)
        """, (name, phone_number, email))
        db.conn.commit()

    @classmethod
    def get_all_contacts(cls):
        db = Database()
        db.cursor.execute("SELECT * FROM contacts")
        return db.cursor.fetchall()

    @classmethod
    def get_contacts_by_group(cls, group_id):
        db = Database()
        db.cursor.execute("""
            SELECT contacts.id, contacts.name, contacts.phone_number, contacts.email
            FROM contacts
            JOIN contact_group ON contacts.id = contact_group.contact_id
            WHERE contact_group.group_id = ?
        """, (group_id,))
        return db.cursor.fetchall()

    @classmethod
    def find_contact_by_id(cls, contact_id):
        db = Database()
        db.cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
        return db.cursor.fetchone()

    @classmethod
    def delete_contact(cls, contact_id):
        db = Database()
        db.cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
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
    def assign_to_group(cls, contact_id, group_id):
        db = Database()
        db.cursor.execute("""
            INSERT INTO contact_group (contact_id, group_id)
            VALUES (?, ?)
        """, (contact_id, group_id))
        db.conn.commit()

class Group:
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