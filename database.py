import sqlite3
import os

class Database:
    DB_PATH = os.path.join(os.path.dirname(__file__), 'db', 'contacts.db')  # Set the correct path for the DB file

    def __init__(self):
        # Establish the database connection to the 'contacts.db' file in the 'db' folder
        self.conn = sqlite3.connect(self.DB_PATH)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
