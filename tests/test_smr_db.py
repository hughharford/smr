import sqlite3
import os.path
from os import listdir
from os.path import isfile, join

from smr.smr_db import SMR_Database
from smr.params import test_db_dict
from smr.db_ops.sql_commands import smr_db_sql

TEST_DB_PATH = test_db_dict['TEST_DB_PATH']
TEST_DB_NAME = test_db_dict['TEST_DB_NAME']

DB_TABLE_CREATE = smr_db_sql['DB_TABLE_CREATE']
SHOW_ALL_DB_TABLES = smr_db_sql['SHOW_ALL_DB_TABLES']
COUNT_ALL_ROWS = smr_db_sql['COUNT_ALL_ROWS']
SELECT_ALL_DATA = smr_db_sql['SELECT_ALL_DATA']
INSERT_SEARCH_DATA = ''

TEST_DATA = {"search_input": "SE23 3YL",
        "postcode": "SE23 3YL",
        "max_roof_id_number": 722,
        "max_roof_area": 17,
        "max_roof_number_panels": 5,
        "total_count_roofs": 723,
        "total_count_panels": 7325
        }


def test_smr_db_extant():
    # need to confirm this test operates
    # intention: instatiated db in SMR_Database
    tester_smr_db = SMR_Database()
    assert tester_smr_db

def test_search_input_to_db():
    # insert search data with 8 values
    INSERT_SEARCH_DATA = f'''
            INSERT INTO searches (
                search_input,
                postcode,
                max_roof_id_number,
                max_roof_area,
                max_roof_number_panels,
                total_count_roofs,
                total_count_panels)

            VALUES
            (
            "{TEST_DATA['search_input']}",
            "{TEST_DATA['postcode']}",
            {TEST_DATA['max_roof_id_number']},
            {TEST_DATA['max_roof_area']},
            {TEST_DATA['max_roof_number_panels']},
            {TEST_DATA['total_count_roofs']},
            {TEST_DATA['total_count_panels']}
            )
            ;
        '''
    tester = SMR_Database()
    tester.establish_smr_db() # create table if not there

    before = tester.run_query(COUNT_ALL_ROWS)[0][0]
    tester.input_search_data(input_sql=INSERT_SEARCH_DATA)
    assert (tester.run_query(COUNT_ALL_ROWS)[0][0] - before) == 1

    # check we can add full initial data, with count of previous searches
    before = tester.run_query(COUNT_ALL_ROWS)[0][0]
    tester.check_n_input_search(data=TEST_DATA)
    assert (tester.run_query(COUNT_ALL_ROWS)[0][0] - before) == 1

if __name__ == "__main__":
    test_search_input_to_db()
