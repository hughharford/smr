import sqlite3
import os.path
from os import listdir
from os.path import isfile, join

from smr.db_ops.operate_db import RunDatabase
from smr.params import test_db_dict
from smr.db_ops.sql_commands import test_db_sql

TEST_DB_PATH = test_db_dict['TEST_DB_PATH']
TEST_DB_NAME = test_db_dict['TEST_DB_NAME']

TEST_DB_TABLE_CREATE = test_db_sql['TEST_DB_TABLE_CREATE']
TEST_SHOW_TABLES = test_db_sql['TEST_SHOW_TABLES']
TEST_COUNT_ROWS = test_db_sql['TEST_COUNT_ROWS']
TEST_CONFIRM_DATA = test_db_sql['TEST_CONFIRM_DATA']
TEST_INCOMPLETE_INSERT = test_db_sql['TEST_INCOMPLETE_INSERT']
TEST_INSERT = test_db_sql['TEST_INSERT']

# 220703 MISSING lines in operate_db:
#  58, 61-82
# DONE, now testing:

def test_operate_db():

    # delete any existing test_NAMED database
    #############################################################
    # print('FOUND FILES:')
    # [print(f) for f in listdir(TEST_DB_PATH)
    #           if isfile(join(TEST_DB_PATH, f))]
    # save all files (mucky for now)
    onlyfiles = [f for f in listdir(TEST_DB_PATH)
                 if isfile(join(TEST_DB_PATH, f))]
    # look to delete only "test_"
    # print('DELETING SPECIFIC FILES:')
    for file in onlyfiles:
        if file[0:5] == 'test_':
            file_for_del = TEST_DB_PATH + '/' + file
            print('going to delete: ' + file_for_del)
            os.remove(file_for_del)
            print('removed ' + file_for_del)

    # assert that no. test_ files == 0
#############################################################
    t_files = [f for f in listdir(TEST_DB_PATH)
               if isfile(join(TEST_DB_PATH, f))]
    count = 0
    for testfile in t_files:
        if testfile[0:5] == 'test_':
            count+=1
    assert count == 0

    # test various __init__ options, create a test_db
#############################################################
    # get db with full db name (as assumed in class)
    db_without_fulldbname = RunDatabase()
    assert db_without_fulldbname
    db_without_fulldbname.close_connection()
    del db_without_fulldbname

    # get db with db name supplied via new connection
    db_with_connection = RunDatabase(
        connection=sqlite3.connect(TEST_DB_NAME))
    assert db_with_connection
    db_with_connection.close_connection()
    del db_with_connection

    # get db with only testname specified
    db_with_testname = RunDatabase(db_name=TEST_DB_NAME)
    assert db_with_testname
    db = db_with_testname # rename for further tests below
    del db_with_testname

    # insert some data, and retrieve a subset to show it worked
#####################################################################
    db.create_table(table_create_sql=TEST_DB_TABLE_CREATE)
    result = db.run_query(query_sql=TEST_SHOW_TABLES)
    assert result[0][0] == 'test_table'

    #     to show that the db exists with the data
    db.insert_data(insert_sql=TEST_INSERT)
    df_result = db.get_content_df(contents_sql=TEST_CONFIRM_DATA)
    assert df_result.shape[0] > 0

    result = db.run_query(query_sql=TEST_COUNT_ROWS)
    assert result[0][0] == 3

    # tidy up and delete the test_db
    db.close_connection()
    del db

if __name__ == "__main__":
    test_operate_db()()
