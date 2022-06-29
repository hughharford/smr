from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
            "End points": ["/save_search", "/view_search"]}

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
            "count_search": count_search,
            "max_roof_id_number": max_roof_id_number,
            "max_roof_area": max_roof_area,
            "max_roof_number_panels": max_roof_number_panels,
            "total_count_roofs": total_count_roofs,
            "total_count_panels": total_count_panels
            }
    # insted of return Logic here will pass abovee data into database
    return data

@app.get("/view_search")
def view_search(search_id):
    # seek clarification on what best parameter here is

    # logic to look up and retrieve information from database

    # Example of type of thing to return (better understanding when DB is built)
    return {'location': {'search_id': search_id, 'city': 'Glasgow', 'lon': 4.2828, 'lat':55.8642},
        'summary': {'num_roofs': 72, 'tot_roof_area': 4321},
        'roof_area': {'roof_1': 300, 'roof_2': 265, 'roof_3': 540}
        }






# example call http://127.0.0.1:8000/pred_postcode?post_code=g4
