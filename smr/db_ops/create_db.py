import sqlite3
import mysql.connector

import pandas as pd

from sql_commands import DB_TABLE_CREATE
from sql_commands import INSERT_INTO_SEARCHES, CONFIRM_DATA
from sql_commands import CHECK_INCOMPLETE_INSERT

from smr.params import params_dict

DB_NAME = 'db/test_database.sqlite'
# db/test_database

class SMR_Database():

    def __init__(self, connection):
        # set default sqlite db
        self.conn = connection
        self.c = conn.cursor()


    def create_database(self):
        self.c = self.conn.cursor()
        self.c.execute(DB_TABLE_CREATE)
        print('Created table within database...  ' + DB_NAME)
        self.conn.commit()

    def create_mysql_db(self):
        # set mysql db
        # PARKED, still to set up mysql and get permissions etc working
        # also, note, would need to set these up on the container too...
        mydb = mysql.connector.connect(
            host=params_dict['HOST'],
            user=params_dict['USER'],
            password=params_dict['PASSWORD']
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE test_mysql_db")

    def insert_data(self):
        self.c.execute(INSERT_INTO_SEARCHES)
        self.conn.commit()

    def insert_incomplete_data(self):
        self.c.execute(CHECK_INCOMPLETE_INSERT)
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
        # db.create_database()
        db.create_mysql_db()
        # db.insert_data()
        # db.insert_incomplete_data()
        # db.confirm_contents()

    except Exception as e:
        print(e)

    finally:
        if conn != None:
            pass
    try:
        conn.close() # <-- This is important
    except Exception:
        print(Exception)
