# not needed in sqlite
#                  DB_CREATE = 'CREATE DATABASE test_database'

DB_TABLE_CREATE = '''CREATE TABLE IF NOT EXISTS searches
(
   ID INT PRIMARY KEY,
   search_input TEXT NOT NULL,
   postcode BOOLEAN DEFAULT "empty",
   count_search INTEGER DEFAULT 1,
   max_roof_id_number INTEGER DEFAULT 0,
   max_roof_area INTEGER DEFAULT 0,
   max_roof_number_panels INTEGER DEFAULT 0,
   total_count_roofs INTEGER DEFAULT 0,
   total_count_panels INTEGER DEFAULT 0,

   UNIQUE (ID, postcode)
);'''


SELECT_ALL_DATA = '''
            SELECT
            search_input,
            postcode,
            count_search
            FROM searches
          '''

COUNT_ALL_ROWS = '''
    SELECT
    count (*)
    FROM searches;
    '''

COUNT_POSTCODE_STUB = '''
    SELECT
    count (*)
    FROM searches
    WHERE postcode LIKE 
    '''


SHOW_ALL_DB_TABLES = '''
    SELECT name FROM sqlite_master
    WHERE type="table"
    ORDER BY name;
    '''

smr_db_sql = {
    'DB_TABLE_CREATE': DB_TABLE_CREATE,
    'SHOW_ALL_DB_TABLES': SHOW_ALL_DB_TABLES,
    'COUNT_ALL_ROWS': COUNT_ALL_ROWS,
    'SELECT_ALL_DATA': SELECT_ALL_DATA,
    'COUNT_POSTCODE_STUB': COUNT_POSTCODE_STUB,
    }

##############################################

##############################################


TEST_DB_TABLE_CREATE = '''CREATE TABLE IF NOT EXISTS test_table
(
   ID INT PRIMARY KEY,
   search_input TEXT NOT NULL,
   postcode BOOLEAN DEFAULT "empty",
   count_search INTEGER DEFAULT 1,
   max_roof_id_number INTEGER DEFAULT 0,
   max_roof_area INTEGER DEFAULT 0,
   max_roof_number_panels INTEGER DEFAULT 0,
   total_count_roofs INTEGER DEFAULT 0,
   total_count_panels INTEGER DEFAULT 0,

   UNIQUE (ID, postcode)
);'''

TEST_INSERT = '''
        INSERT INTO test_table (
            search_input,
            postcode,
            count_search)

        VALUES
        ('SE23 3YL','SE23 3YL', 45),
        ('G3 xxx','G3 xxx', 1001),
        ('latt long','SE23 3YL', 23)
        ;
    '''

TEST_CONFIRM_DATA = '''
            SELECT
            search_input,
            postcode,
            count_search
            FROM test_table
            WHERE search_input = "SE23 3YL"
          '''

TEST_INCOMPLETE_INSERT = '''
        INSERT INTO test_table (
            search_input
            )
        VALUES
        ('latt long')
        ;
'''

TEST_SHOW_TABLES = '''
    SELECT name FROM sqlite_master
    WHERE type="table"
    ORDER BY name;
    '''

TEST_COUNT_ROWS = '''
    SELECT
    count (*)
    FROM test_table;
    '''

test_db_sql = {
    'TEST_DB_TABLE_CREATE': TEST_DB_TABLE_CREATE,
    'TEST_SHOW_TABLES': TEST_SHOW_TABLES,
    'TEST_COUNT_ROWS': TEST_COUNT_ROWS,
    'TEST_CONFIRM_DATA': TEST_CONFIRM_DATA,
    'TEST_INCOMPLETE_INSERT': TEST_INCOMPLETE_INSERT,
    'TEST_INSERT': TEST_INSERT,
    }
