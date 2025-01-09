from database import Database

class Group:
    def __init__(self, group_id, name):
        self.id = group_id
        self.name = name

    @classmethod
    def create_table(cls):
        db = Database()
        query = """
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
        db.execute_query(query)

    @classmethod
    def add_group(cls, name):
        db = Database()
        query = "INSERT INTO groups (name) VALUES (?)"
        db.execute_query(query, (name,))

    @classmethod
    def get_all_groups(cls):
        db = Database()
        query = "SELECT * FROM groups"
        rows = db.execute_query(query)
        return [cls.from_db_row(row) for row in rows]  # Use from_db_row method

    @classmethod
    def find_group_by_id(cls, group_id):
        db = Database()
        query = "SELECT * FROM groups WHERE id = ?"
        rows = db.execute_query(query, (group_id,))
        return cls.from_db_row(rows[0]) if rows else None  # Use from_db_row method

    @classmethod
    def delete_group(cls, name):
        db = Database()
        query = "DELETE FROM groups WHERE name = ?"
        db.execute_query(query, (name,))

    @classmethod
    def from_db_row(cls, row):
        return cls(row[0], row[1])
