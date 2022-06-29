import sqlite3
import mysql.connector

import pandas as pd

from smr.db_ops.sql_commands import DB_TABLE_CREATE
from smr.db_ops.sql_commands import INSERT_INTO_SEARCHES, CONFIRM_DATA
from smr.db_ops.sql_commands import CHECK_INCOMPLETE_INSERT

from smr.params import db_dict, test_db_dict

DB_PATH = db_dict['DB_PATH']
DB_NAME = db_dict['DB_NAME']
TEST_DB_PATH = test_db_dict['TEST_DB_PATH']
TEST_DB_NAME = test_db_dict['TEST_DB_NAME']

class SMR_Database():

    def __init__(self, connection='', db_name=''):
        # set default sqlite db
        if db_name == TEST_DB_NAME:
            # create test
            self.conn = sqlite3.connect(TEST_DB_NAME, timeout=0.00001)
            print('Connected to database...  ' + TEST_DB_NAME)
            self.get_cursor()

        elif connection=='' and db_name == '':
            # create db connection
            self.conn = sqlite3.connect(DB_NAME, timeout=0.00001)
            print('Connected to database...  ' + DB_NAME)
            self.get_cursor()
        else:
            self.conn = connection
            self.c = conn.cursor()


    def get_cursor(self):
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute(DB_TABLE_CREATE)
        print('Created table...  ')
        self.conn.commit()

    def insert_data(self):
        print('Inserted data...  ')
        self.c.execute(INSERT_INTO_SEARCHES)
        self.conn.commit()

    def insert_incomplete_data(self):
        print('Inserted incomplete data...  ')
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
        db.get_cursor()
        db.create_table()

        db.insert_data()
        # # update this to take and then input values


        db.insert_incomplete_data()
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
