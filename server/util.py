import json
import pickle
import numpy as np

# global variables
__locations=None
__data_columns=None
__model=None

# routine for predicting the price based on location, sqft, bhk, bath
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())      # convert locations to lowercase
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

# this will contain all the locations
def get_locations():
    return __locations

# it will load columns and the model
def load_saved_artifacts():
    print("Loading saved artifacts...start!")
    global __data_columns
    global __locations
    global __model

    with open("./resources/columns.json",'r') as f:
        __data_columns = json.load(f)["data columns"]       # json will return a dictionary. store all the columns
        __locations = __data_columns[3:]        # all the locations start from index=3

    with open("./resources/price_prediction_model.pickle","rb") as f:
        __model = pickle.load(f)        # load the model too
    print("Loading saved artifacts...done!!")

if __name__=="__main__":
    load_saved_artifacts()
    print(get_locations())
    # try some parameters
    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))
    print(get_estimated_price("Kalhalli", 1000, 2, 2))
    print(get_estimated_price("Ejipura", 1000, 2, 2))