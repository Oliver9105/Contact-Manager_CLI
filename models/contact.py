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