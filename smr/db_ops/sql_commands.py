# not needed in sqlite
#                  DB_CREATE = 'CREATE DATABASE test_database'

DB_TABLE_CREATE = '''CREATE TABLE IF NOT EXISTS searches
(
   ID INT PRIMARY KEY NOT NULL,
   [search_input] TEXT NOT NULL,
   [postcode] BOOLEAN NOT NULL,
   [count_search] INTEGER,
   UNIQUE (ID, postcode)
);'''

DB_TABLE_CREATE_SHORT = '''CREATE TABLE IF NOT EXISTS searches
(
   ID INT PRIMARY KEY,
   [search_input] TEXT NOT NULL,
   [postcode] TEXT NOT NULL,
   [count_search] INTEGER
);'''


INSERT_INTO_SEARCHES = '''
        INSERT INTO searches (
            search_input,
            postcode,
            count_search)

        VALUES
        ('SE23 3YL','SE23 3YL', 45),
        ('G3 xxx','G3 xxx', 1001),
        ('latt long','SE23 3YL', 23)
        ;
    '''

CONFIRM_DATA = '''
            SELECT
            search_input,
            postcode,
            count_search
            FROM searches
          '''
