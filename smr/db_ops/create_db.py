import sqlite3
import pandas as pd

from sql_commands import DB_TABLE_CREATE, DB_TABLE_CREATE_SHORT
from sql_commands import INSERT_INTO_SEARCHES, CONFIRM_DATA


DB_NAME = 'db/test_database.sqlite'
# db/test_database

class SMR_Database():

    def __init__(self, connection):
        self.conn = connection

    def create_database(self):
        self.c = self.conn.cursor()
        self.c.execute(DB_TABLE_CREATE)
        print('Created table within database...  ' + DB_NAME)
        self.conn.commit()
        print('Commit made >>')

    def insert_data(self):
        self.c.execute(INSERT_INTO_SEARCHES)
        self.conn.commit()


    def confirm_contents(self):
        self.c.execute(CONFIRM_DATA)
        df = pd.DataFrame(
            self.c.fetchall(),
            columns=['search_input','postcode', 'count_search'])
        print (df)

if __name__ == "__main__":

    conn = sqlite3.connect(DB_NAME, timeout=0.00001)
    print('Connected to database...  ' + DB_NAME)

    try:
        db = SMR_Database(conn)
        db.create_database()
        db.insert_data()
        db.confirm_contents()

    except Exception as e:
        print(e)

    finally:
        if conn != None:
            pass
    try:
        conn.close() # <-- This is important
    except Exception:
        print(Exception)
