import mysql.connector

# make sure to start mysql on the command line:
#
#                sudo systemctl start mysql.service
#

cnx = mysql.connector.connect(user='hsth', password='',
                              host='127.0.0.1',
                              database='test_db')
cnx.close()


# gets:
#
# mysql.connector.errors.ProgrammingError:
# 1698 (28000):
# Access denied for user 'hsth'@'localhost'
#
# i.e. permissions for users not set yet
