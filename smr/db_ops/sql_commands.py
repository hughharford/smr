# not needed in sqlite
#                  DB_CREATE = 'CREATE DATABASE test_database'

DB_TABLE_CREATE = '''CREATE TABLE searches (   /* Create table with multiple fields as unique */
   ID INT NOT NULL
   search_input VARCHAR(255) NOT NULL
   postcode BOOLEAN NOT NULL
   count_search INT(255)
   UNIQUE (ID, postcode)
);'''
