import os.path
from os import listdir
from os.path import isfile, join

from smr.db_ops.operate_db import SMR_Database
from smr.params import test_db_dict

TEST_DB_PATH = test_db_dict['TEST_DB_PATH']
TEST_DB_NAME = test_db_dict['TEST_DB_NAME']

def test_database_is_created():

    # delete any existing test_NAMED database
    #############################################################
    # print('FOUND FILES:')
    # [print(f) for f in listdir(TEST_DB_PATH) if isfile(join(TEST_DB_PATH, f))]
    # save all files (mucky for now)
    onlyfiles = [f for f in listdir(TEST_DB_PATH) if isfile(join(TEST_DB_PATH, f))]
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
    testfiles = [f for f in listdir(TEST_DB_PATH) if isfile(join(TEST_DB_PATH, f))]
    count = 0
    for testfile in testfiles:
        if testfile[0:5] == 'test_':
            count+=1
    assert count == 0
    # create a test_db
#############################################################
    db = SMR_Database(db_name=TEST_DB_NAME)
    # assert that it exists


    # add some data
    # then retrieve a subset
    #     to show that the db exists with the data

    # tidy up and delete the test_db
    pass

if __name__ == "__main__":
    test_database_is_created()
