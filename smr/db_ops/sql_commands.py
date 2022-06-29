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

            )

        VALUES
        ('latt long')
        ;
'''

CONFIRM_DATA = '''
            SELECT
            search_input,
            postcode,
            count_search
            FROM searches
          '''

CONFIRM_GL8_POSTCODE_SEARCH_COUNT_ZERO = '''
            SELECT
            search_input,
            postcode,
            count_search
            FROM searches
            WHERE postcode = "GL8"
          '''
