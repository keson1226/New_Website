#### Import------------------------------
# Import Module
from copy import deepcopy

# Import MongoDB Setting Module
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Import Data Schema
from web_backend.schema.hot_key_response_schema import HotKeyResponseModel

# Import Type Fixer
from web_backend.db_control.type_fixer import hot_key_type_fixer



#### Create Communication With MongoDB Server------------------------------
# Build MongoDB Server Address
username = "fastapi"
password = "JuZ9zAUjoKvd1Ugp"
url = f"mongodb+srv://{username}:{password}@buffer.pfogvl4.mongodb.net/?retryWrites=true&w=majority"

# Build Communication
client = MongoClient(url, server_api=ServerApi(version='1'))

# Alert Connect Info
try:
    client.admin.command('ping') ## Ping server
    print("Pinged your deployment. You successfully connected to MongoDB!\n")
except Exception as e:
    print(e)



#### Hot Key Database------------------------------
# Set Database to "hot_key"
hot_key_db = client.hot_key

# Insert Data
async def insert_hot_key(hot_keys:HotKeyResponseModel) -> bool: 
    geo = hot_key_db[hot_keys.geo] ## from database choose collection {hot_keys.geo}

    hot_keys = deepcopy(hot_keys) ## make data copy
    hot_keys = hot_key_type_fixer(hot_keys) ## change data type into dict

    for day_hot_key in hot_keys['day_list']:
        # check database data status
        if geo.find_one({"day_date_int":day_hot_key['day_date_int']}): ## database found old data
            geo.update_one({"day_date_int": day_hot_key['day_date_int']}, {"$set": day_hot_key}) ## use this data update old data

        else: ## database has no old data
            geo.insert_one(day_hot_key) ## insert this data
    
    return True
