import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from smr.smr_db import SMR_Database
from smr.db_ops.sql_commands import select_by_postcode
app = FastAPI()

COLUMN_NAMES = {0:'ID', 1:'search_input', 2:'postcode',
               3:'count_search', 4:'max_roof_id_number',
               5:'max_roof_area', 6:'max_roof_number_panels',
               7:'total_count_roofs', 8:'total_count_panels'}


# add_middleware will allow calls from the JavaScript of a webpage
# see 1 - Build your API for more info
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # allows all origins
    allow_credentials=True,
    allow_methods=['*'], # allow all methods
    allow_headers=['*'], # allows all headers
)

# "Home" Page
@app.get("/")
def index():
    return {"Welcome": "to our Solar My Roof API",
            "End points": ["/save_search", "/view_search", "/view_all"]}

@app.get("/save_search")
def save_search(search_input, postcode, count_search: int, max_roof_id_number: int,
                max_roof_area: int, max_roof_number_panels: int, total_count_roofs: int,
                total_count_panels: int):
    """
    Save meta data of search to database
    """
    # put params into a database
    data = {"search_input": search_input,
            "postcode": postcode,
            "max_roof_id_number": max_roof_id_number,
            "max_roof_area": max_roof_area,
            "max_roof_number_panels": max_roof_number_panels,
            "total_count_roofs": total_count_roofs,
            "total_count_panels": total_count_panels
            }


    # insted of return Logic here will pass above data into database
    # smr_db = SMR_Database()
    # smr_db.check_n_input_search(data)
    return data


@app.get("/view_search")
def view_search(postcode):
    # example call http://127.0.0.1:8000/view_search?postcode=SE23 3YL

    # Return SQL Query to retrieve all columns from database
    # under post code.
    SELECT_BY_POSTCODE = select_by_postcode(postcode)
    # = ''' SELECT *; FROM searches WHERE postcode = "postcode";

    # Create a class instance:
    smr_db = SMR_Database()
    prev_search_df = smr_db.get_content_df(contents_sql=SELECT_BY_POSTCODE)
    smr_db.close_connection()

    # maniuplate dataframe to format in a suitable dictionary.
    # - remove duplicates here (should be removed at later date when database
    # overwrites similar post codes and not create duplicates).
    prev_search_df.rename(columns=COLUMN_NAMES, inplace=True)
    prev_search_df.drop_duplicates(subset='postcode', keep='last', inplace=True)

    postcode_dict = {}
    for index, row in prev_search_df.iterrows():
        print('index ', index)
        print('row ', row['search_input'])

        postcode_dict[row['postcode']] = {"ID": row['ID'] ,
                                        "count":row['count_search'] ,
                                        "max_roof_id_number": row['max_roof_id_number'],
                                        "max_roof_area":row['max_roof_area'],
                                        "max_roof_number_panels": row['max_roof_number_panels'],
                                        "total_count_roofs": row['total_count_roofs'],
                                        "total_count_panels": row['total_count_panels']}

    return postcode_dict

@app.get("/view_all")
def view_all():
    # example call http://127.0.0.1:8000/view_all
    # SELECT_ALL_DATA from sql queries is only selecting 3 columns
    SELECT_ALL_DATA = '''
            SELECT *
            FROM searches
          '''
    # Create a class instance:
    smr_db = SMR_Database()
    all_data_df = smr_db.get_content_df(contents_sql=SELECT_ALL_DATA)
    smr_db.close_connection()


    # see comment in view_search() regarding df manipulation
    all_data_df.rename(columns=COLUMN_NAMES, inplace=True)
    all_data_df.drop_duplicates(subset='postcode', keep='last', inplace=True)

    all_data_dict = {}
    for index, row in all_data_df.iterrows():
        all_data_dict[row['postcode']] = {"ID": [index, row['ID']], # index here can go
                                        "count":row['count_search'] ,
                                        "max_roof_id_number": row['max_roof_id_number'],
                                        "max_roof_area":row['max_roof_area'],
                                        "max_roof_number_panels": row['max_roof_number_panels'],
                                        "total_count_roofs": row['total_count_roofs'],
                                        "total_count_panels": row['total_count_panels']}

    return all_data_dict
