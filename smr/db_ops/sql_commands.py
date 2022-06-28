# not needed in sqlite
#                  DB_CREATE = 'CREATE DATABASE test_database'

DB_TABLE_CREATE = '''CREATE TABLE IF NOT EXISTS searches
(
   ID INT PRIMARY KEY NOT NULL,
   [search_input] TEXT NOT NULL,
   [postcode] BOOLEAN NOT NULL,
   [count_search] INTEGER DEFAULT 0,
   UNIQUE (ID, postcode)
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

CHECK_INCOMPLETE_INSERT = '''
        INSERT INTO searches (
            search_input
            , postcode
            )

        VALUES
        ('latt long','GL8')
        ;
'''

CONFIRM_DATA = '''
            SELECT
            search_input,
            postcode,
            count_search
            FROM searches
          '''
