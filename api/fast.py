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

@app.get("/")
def index():
    return {"Welcome": "to our Solar My Roof API"}

@app.get("/pred_postcode")
def read_postcode(post_code):
    # any string manipulation
    post_code = post_code.lower() # etc...

    # call our database and retrieve info such as:
    # lat, lon, num_roofs, foreachroof - area
    # try: logic to search databse for post code
    # i.e., we want to check if a prediciton on this post_code has been done
    # alredy. If so, we want to extract meta data from SQL database

    #except: load and call model to receive meta data
    # make sure that all meta data is then stored in DB for future use
    # import model etc call model ........

    return {'location': {'city': 'Glasgow', 'lon': 4.2828, 'lat':55.8642},
            'summary': {'num_roofs': 72, 'tot_roof_area': 4321},
            'roof_area': {'roof_1': 300, 'roof_2': 265, 'roof_3': 540}
            }

@app.get("/save_search")
def save_search(params):
    # put params into a database
    pass

# example call http://127.0.0.1:8000/pred_postcode?post_code=g4
