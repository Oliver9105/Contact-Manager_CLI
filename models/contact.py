from models.group import Group
from database import Database

class Contact:
    def __init__(self, contact_id, name, phone_number, email):
        self.id = contact_id
        self.name = name
        self.phone_number = phone_number
        self.email = email

    @classmethod
    def create_table(cls):
        query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
        Database().execute_query(query)

    @classmethod
    def add_contact(cls, name, phone_number, email):
        query = "INSERT INTO contacts (name, phone_number, email) VALUES (?, ?, ?)"
        Database().execute_query(query, (name, phone_number, email))

    @classmethod
    def get_all_contacts(cls):
        query = "SELECT * FROM contacts"
        rows = Database().execute_query(query)
        return [cls.from_db_row(row) for row in rows]  # Use from_db_row method

    @classmethod
    def get_contacts_by_group(cls, group_id):
        query = """
        SELECT c.id, c.name, c.phone_number, c.email
        FROM contacts c
        JOIN contact_group cg ON c.id = cg.contact_id
        WHERE cg.group_id = ?
        """
        rows = Database().execute_query(query, (group_id,))
        return [cls.from_db_row(row) for row in rows] if rows else []  # Return a list of contacts

    @classmethod
    def get_groups_for_contact(cls, contact_id):
        db = Database()
        query = """
        SELECT g.id, g.name 
        FROM groups g
        JOIN contact_group cg ON g.id = cg.group_id 
        WHERE cg.contact_id = ?
        """
        rows = db.execute_query(query, (contact_id,))
        return [Group.from_db_row(row) for row in rows] if rows else []  # Ensure correct Group initialization

    @classmethod
    def find_contact_by_id(cls, contact_id):
        query = "SELECT * FROM contacts WHERE id = ?"
        rows = Database().execute_query(query, (contact_id,))
        return cls.from_db_row(rows[0]) if rows else None  # Use from_db_row method

    @classmethod
    def delete_contact(cls, contact_id):
        query = "DELETE FROM contacts WHERE id = ?"
        Database().execute_query(query, (contact_id,))

    @classmethod
    def assign_to_group(cls, contact_id, group_id):
        query = """
        INSERT INTO contact_group (contact_id, group_id)
        VALUES (?, ?)
        """
        try:
            Database().execute_query(query, (contact_id, group_id))
            print(f"Contact {contact_id} has been assigned to group {group_id}.")
        except Exception as e:
            print(f"Error assigning contact to group: {e}")

    @classmethod
    def from_db_row(cls, row):
        return cls(row[0], row[1], row[2], row[3])
