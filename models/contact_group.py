from database import Database

class ContactGroup:
    @classmethod
    def create_table(cls):
        db = Database()
        query = """
        CREATE TABLE IF NOT EXISTS contact_group (
            contact_id INTEGER,
            group_id INTEGER,
            FOREIGN KEY (contact_id) REFERENCES contacts(id),
            FOREIGN KEY (group_id) REFERENCES groups(id),
            PRIMARY KEY (contact_id, group_id)
        )
        """
        db.execute_query(query)

    @classmethod
    def assign_contact_to_group(cls, contact_id, group_id):
        db = Database()
        query = """
        INSERT INTO contact_group (contact_id, group_id)
        VALUES (?, ?)
        """
        db.execute_query(query, (contact_id, group_id))

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
        return [Group.from_db_row(row) for row in rows] if rows else []

    @classmethod
    def get_contacts_for_group(cls, group_id):
        db = Database()
        query = """
        SELECT c.id, c.name, c.phone_number, c.email
        FROM contacts c
        JOIN contact_group cg ON c.id = cg.contact_id
        WHERE cg.group_id = ?
        """
        rows = db.execute_query(query, (group_id,))
        return [Contact.from_db_row(row) for row in rows] if rows else []

    @classmethod
    def remove_contact_from_group(cls, contact_id, group_id):
        db = Database()
        query = """
        DELETE FROM contact_group WHERE contact_id = ? AND group_id = ?
        """
        db.execute_query(query, (contact_id, group_id))

    @classmethod
    def assign_to_group(cls, contact_id, group_id):
        query = """
        INSERT INTO contact_group (contact_id, group_id)
        VALUES (?, ?)
        """
        Database().execute_query(query, (contact_id, group_id))
        print(f"Contact ID {contact_id} successfully assigned to Group ID {group_id}.")
