import sqlite3
import os

class Database:
    def __init__(self, db_file="db/contacts.db"): 
        db_folder = os.path.dirname(db_file) 
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)

        self.conn = sqlite3.connect(db_file) 
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()