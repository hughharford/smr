from smr.db_ops.operate_db import RunDatabase
from smr.params import db_dict
from smr.db_ops.sql_commands import smr_db_sql

INSERT_SEARCH_DATA = ''

class SMR_Database(RunDatabase):
    '''
    SMR database class, storing and retrieving data.
    Uses params and sql_commands for SQL strings etc
    '''

    def __init__(self):
        '''
        RunDatabase assumes SQLite below
        '''
        super().__init__(db_name=db_dict['DB_NAME'])


    def establish_smr_db(self):
        pass
        # self.create_table(table_create_sql=db_dict['DB_TABLE_CREATE'])

    def check_n_input_search(self, data):
        count_sql = smr_db_sql['COUNT_POSTCODE_STUB']+'"'+data['postcode']+'";'
        count_of_postcode_searches_made = self.run_query(query_sql=count_sql)[0][0]
        print(f'searches_made: {count_of_postcode_searches_made}')

        INSERT_SEARCH_DATA = f'''
                INSERT INTO searches (
                    search_input,
                    postcode,
                    count_search,
                    max_roof_id_number,
                    max_roof_area,
                    max_roof_number_panels,
                    total_count_roofs,
                    total_count_panels)

                VALUES
                (
                "{data['search_input']}",
                "{data['postcode']}",
                {count_of_postcode_searches_made},
                {data['max_roof_id_number']},
                {data['max_roof_area']},
                {data['max_roof_number_panels']},
                {data['total_count_roofs']},
                {data['total_count_panels']}
                )
                ;
            '''
        self.input_search_data(INSERT_SEARCH_DATA)

    def input_search_data(self, input_sql=INSERT_SEARCH_DATA):
        if input_sql:
            self.run_query(query_sql=input_sql)
        # account for count_search!

# if __name__ == "__main__":
#     db = SMR_Database()
