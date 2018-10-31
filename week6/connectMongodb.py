import pymongo
import urllib
from pymongo import MongoClient

username = urllib.parse.quote_plus('zouyang')
password = urllib.parse.quote_plus('xr44nHj8')

# client = MongoClient('mongodb://%s:%s@localhost:27017/?authSource=zouyangdb'% (username,password))
client = MongoClient('mongodb://%s:%s@smgo7db01.smu.edu:27017/?authSource=zouyangdb'% (username,password))

db = client.zouyangdb

collection = db.collection_names(include_system_collections=False)
for collect in collection:
    print(collect)

print("Success")
# http://smgo7db01.smu.edu/