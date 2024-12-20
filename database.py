import sqlite3

class Database:
  def __init__(self):
    self.conn = sqlite3.connect("contacts.db")
    self.cursor = self.conn.cursor()

  def close(self):
    self.conn.close()