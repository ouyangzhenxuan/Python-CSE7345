import pymongo
import urllib
from pymongo import MongoClient
import json



def createDatabase():
    client = MongoClient('localhost', 27017)
    mydb = client["seconddatabase"]
    mycol = mydb["customers"]

def insertData():
    client = MongoClient('localhost', 27017)
    mydb = client["seconddatabase"]
    mycol = mydb["customers"]

    # Create the information to be inserted
    mydict = {"name":"David", "address":"Dallas"}
    # Insert the information into collections
    data = mycol.insert_one(mydict)


def accessData_mongodb():
    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['seconddatabase']
    # Select the Collections
    collection = db['customers']
    result = collection.find()

    for i in result:
        print(i)

if __name__ == "__main__":
    # createDatabase()
    # insertData()
    accessData_mongodb()

