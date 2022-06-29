import mysql.connector
from smr.params import params_dict

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

def create_mysql_db(self):
    # set mysql db
    # PARKED, still to set up mysql and get permissions etc working
    # also, note, would need to set these up on the container too...
    mydb = mysql.connector.connect(
        host=params_dict['HOST'],
        user=params_dict['USER'],
        password=params_dict['PASSWORD']
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE test_mysql_db")
