import sqlite3
from sql_commands import DB_TABLE_CREATE

DB_NAME = 'db/test_database'
# db/test_database

class SMR_Database():

    def __init__(self):
        pass

    def create_database(self):
        conn = sqlite3.connect(DB_NAME, timeout=3)
        print('Connected to database...  ' + DB_NAME)
        c = conn.cursor()

        c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
          ''')
        print('Created table within database...  ' + DB_NAME)

        conn.commit()
        conn.close()

if __name__ == "__main__":
    db = SMR_Database()
    db.create_database()
