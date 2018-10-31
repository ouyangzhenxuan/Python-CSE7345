import pymongo
import urllib
from pymongo import MongoClient
import  pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

def findCloestCity():
    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['mongoindex']
    # Select the Collections
    collection = db['zipstates']
    result = collection.find({},{'city':1, 'longitude':1, 'latitude':1, '_id':0})
    # for i in result:
    #     print(i)
    df = pd.read_csv("/Users/ouyang/Desktop/CSE7345PythonProgramming/week7/mysteryLatLong.txt")
    mylist = []
    tmplat = []
    tmplong = []
    distance1 = []
    distance2 = []
    distance3 = []
    tmp_mindis = 0
    km = 0
    for i in df.loc[:]:
        mylist.append(float(i))

    for j in range(0, len(mylist)):
        if j%2==0:
            tmplat.append(mylist[j])
        else:
            tmplong.append(mylist[j])
    count = 0
    for p in range(0, len(tmplong)):
        distance1 = []
        print("hello")
        result = collection.find({}, {'city': 1, 'longitude': 1, 'latitude': 1, '_id': 0})
        for q in result:
            tmpdict = {}
            tmpdict = q
            longi = tmpdict.get("longitude")
            lati = tmpdict.get("latitude")
            cit = tmpdict.get("city")
            if longi != None:
                km = calculateDist(longi, lati, tmplong[p], tmplat[p])
                # print(longi)
                distance1.append(km)
            # tmp_mindis = min(distance1)
        print(min(distance1))
        # print(tmplong[p])
        # print(tmplat[p])
        # print(tmp_mindis)
    # print(distance2)

from math import radians, cos, sin, asin, sqrt
def calculateDist(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    # Radius of the earth is 6371 km
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km

def mapfuncTest():
    items = [1,2,3,4,5]
    result = list(map(lambda x: x**2, items))
    print(result)
    result2 = list(map(lambda x: x<3, items))
    print(result2)

# findCloestCity()
mapfuncTest()