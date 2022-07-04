import sqlite3
import mysql.connector

import pandas as pd

from smr.params import db_dict, test_db_dict

DB_PATH = db_dict['DB_PATH']
DB_NAME = db_dict['DB_NAME']
TEST_DB_PATH = test_db_dict['TEST_DB_PATH']
TEST_DB_NAME = test_db_dict['TEST_DB_NAME']

class RunDatabase():
    '''
    Utility database class to operate the SQLite.

    Initiate, with or without db connection parameter
    Then pass sql to the various methods, a get the .fetchall() returned

    We can refactor here to add a different db provider/type if we want
    '''

    def __init__(self, connection='', db_name=''):
        # default sqlite db
        if db_name == TEST_DB_NAME or db_name == DB_NAME:
            # create test
            self.conn = sqlite3.connect(db_name, timeout=0.00001)
            print('Connected to database...  ' + db_name)
            self.get_cursor()

        elif connection=='' and db_name == '': # assume smr database
            # create db connection
            self.conn = sqlite3.connect(DB_NAME, timeout=0.00001)
            print('Connected to database...  ' + DB_NAME)
            self.get_cursor()
        else:
            self.conn = connection
            self.get_cursor()

    def get_cursor(self):
        self.c = self.conn.cursor()

    def create_table(self, table_create_sql=''):
        if table_create_sql:
            self.c.execute(table_create_sql)
            self.conn.commit()
            print('Created table...  ')

    def run_query(self, query_sql=''):
        if query_sql:
            self.c.execute(query_sql)
            self.conn.commit()
            print('Ran your query:  >>>> ' + query_sql)
            return self.c.fetchall()

    def insert_data(self, insert_sql=''):
        if insert_sql:
            self.c.execute(insert_sql)
            self.conn.commit()
            print('Inserted data:  >>>> ' + insert_sql)

    def get_content_df(self, contents_sql=''):
        if contents_sql:
            self.c.execute(contents_sql)
            df = pd.DataFrame(self.c.fetchall())
            return df

    def close_connection(self):
        if self.conn != None:
            self.conn.close() # <-- This is important.

if __name__ == "__main__":
    pass
    # conn = sqlite3.connect(DB_NAME, timeout=0.00001)
    # print('Connected to database...  ' + DB_NAME)

    # try:
    #     db = RunDatabase(conn)
    #     db.get_cursor()
    #     db.create_table()
    #     db.insert_data()
    #     db.get_content_df()
    # except Exception as e:
    #     print(e)

    # try:
    #     conn.close() # <-- This is important
    # except Exception:
    #     print(Exception)
