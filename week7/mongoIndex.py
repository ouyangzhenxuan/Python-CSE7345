import pymongo
import urllib
from pymongo import MongoClient
import  pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

def indexQuery():
    df = pd.read_csv("/Users/ouyang/Desktop/CSE7345PythonProgramming/week7/zipcodes.states.gps.csv")
    print(df)

def acessData():
    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['mongoindex']
    # Select the Collections
    collection = db['zipstates']
    result = collection.find()
    for i in result:
        print(i)

def createDatabase():
    client = MongoClient('localhost', 27017)
    mydb = client["mongoindex"]
    mycol = mydb["indextest"]

###################################################################
# Create a collection called "zipstates" and import .csv into it
def insertData():
    client = MongoClient('localhost', 27017)
    mydb = client["mongoindex"]
    mycol = mydb["zipstates"]
    data = pd.read_csv("/Users/ouyang/Desktop/CSE7345PythonProgramming/week7/zipcodes.states.gps.csv")
    # Transfer Datafame to json format
    payload = json.loads(data.to_json(orient='records'))
    # Insert the data into 'mycol' collection
    mycol.insert(payload)
    return mycol.count()

# Find the city and state of "zip_code=10463"
def searchdb():
    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['mongoindex']
    # Select the Collections
    collection = db['zipstates']
    result = collection.find({"zip_code": 10463}, {"zip_code":1 ,"state":1, "city":1})
    # print(result)
    for i in result:
        print(i)

# Set two global value
totalDocs_NoIndex = []
execTime_NoIndex = []

# Get the docsNum and execTime of NoIndex
def func_Explain_NoIndex():
    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['mongoindex']
    # Select the Collections
    collection = db['zipstates']
    result = collection.find({"zip_code": 10463}, {"zip_code":1 ,"state":1, "city":1})
    explainMsg = result.explain()["executionStats"]
    global totalDocs_NoIndex
    totalDocs_NoIndex.append(explainMsg.get("totalDocsExamined"))
    global execTime_NoIndex
    execTime_NoIndex.append(explainMsg.get("executionTimeMillis"))
    # The return of explain is a dictionary
    print("totalDocsExamined_NoIndex: ", end="")
    print(explainMsg.get("totalDocsExamined"))
    print("executionTimeMillis_NoIndex: ", end="")
    print(explainMsg.get("executionTimeMillis"))

# Get the docsNum and execTime of Index
def func_Explain_Index():
    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['mongoindex']
    # Select the Collections
    collection = db['indextest']

    # Create index for 'zip_code' in Ascending order
    indexCreate = collection.create_index([("zip_code", pymongo.ASCENDING)])

    result = collection.find({"zip_code": 10463}, {"zip_code": 1, "state": 1, "city": 1})
    explainMsg = result.explain()["executionStats"]
    global totalDocs_NoIndex
    totalDocs_NoIndex.append(explainMsg.get("totalDocsExamined"))
    global execTime_NoIndex
    execTime_NoIndex.append(explainMsg.get("executionTimeMillis"))
    print("totalDocsExamined: ", end="")
    print(explainMsg.get("totalDocsExamined"))
    print("executionTimeMillis: ", end="")
    print(explainMsg.get("executionTimeMillis"))

# Plot the comparison of totalDocsExamined between NoIndex and Index
def plot_totalDocsExam():
    frequencies = totalDocs_NoIndex
    freq_series = pd.Series(frequencies)

    x_labels = ["NoIndex", "Index"]
    plt.figure(figsize=(8, 6))
    ax = freq_series.plot(kind='bar')
    ax.set_title('The totalDocsExamined')
    # ax.set_xlabel()
    ax.set_ylabel('DocsNumber')
    ax.set_xticklabels(x_labels)
    rects = ax.patches

    # For each bar: Place a label
    for rect in rects:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = 5
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        plt.annotate(
            label,  # Use `label` as label
            (x_value, y_value),  # Place label at end of the bar
            xytext=(0, space),  # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',  # Horizontally center label
            va=va)  # Vertically align label differently for
        # positive and negative values.
    plt.show()

# Plot the comparison of executionTimemillis between NoIndex and Index
def plot_exeTime():
    frequencies = execTime_NoIndex
    freq_series = pd.Series(frequencies)

    x_labels = ["NoIndex", "Index"]
    plt.figure(figsize=(8, 6))
    ax = freq_series.plot(kind='bar', color = 'red')
    ax.set_title('The executiontimeMillis')
    # ax.set_xlabel()
    ax.set_ylabel('executiontimeMillis')
    ax.set_xticklabels(x_labels)
    rects = ax.patches

    # For each bar: Place a label
    for rect in rects:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = 5
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        plt.annotate(
            label,  # Use `label` as label
            (x_value, y_value),  # Place label at end of the bar
            xytext=(0, space),  # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',  # Horizontally center label
            va=va)  # Vertically align label differently for
        # positive and negative values.
    plt.show()

def insert_zipcodes():
    client = MongoClient('localhost', 27017)
    mydb = client["mongoindex"]
    mycol = mydb["zipcodes"]
    data = pd.read_csv("/Users/ouyang/Desktop/CSE7345PythonProgramming/week7/zipcodes.states.gps.csv")
    payload = json.loads(data.to_json(orient='records'))
    mycol.insert(payload)
    return mycol.count()

# Find the city based on the zipcodes in the .txt file
def find_city_BaseOnZipcodes():
    # ff = np.loadtxt("/Users/ouyang/Desktop/CSE7345PythonProgramming/week7/zipcodes.txt")
    zipc = pd.read_csv("/Users/ouyang/Desktop/CSE7345PythonProgramming/week7/zipcodes.txt", header=None)
    zipcodes = []

    # Put the zipcodes of .txt in a list
    for i in zipc.loc[0]:
        zipcodes.append(i)

    df = pd.DataFrame(columns=["Zip", "City", "State"])

    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['mongoindex']
    # Select the Collections
    collection = db['zipstates']
    mydict = {}

    for i in zipcodes:
        result = collection.find({"zip_code": i}, {"zip_code": 1, "state": 1, "city": 1, "_id": 0})
        # Store the return object in a dictionary
        for j in result:
            # Type of i is dict
            mydict = j

        tmp_zipcodes = i
        city = mydict.get("city")
        state = mydict.get("state")
        # If mydict is NULL, then "city" will be None
        if city == None:
            city = "NOT"
            state = "VALID Zip"

        # Use the append() of DataFrame to add data into df
        df2 = pd.DataFrame([[str(tmp_zipcodes).zfill(5), city, state]], columns=["Zip", "City", "State"])
        df = df.append(df2, ignore_index=True)
        mydict = {}
    print(df)

# Find the closest city according to the GPS coordinate
def find_CloestCity():
    mylist = []
    tmplat = []
    tmplong = []
    minDict = {"longitude": 0, "latitude": 0, "city": "", 'state': "", "zipcode": 0}

    # Connect to the local database
    client = MongoClient('localhost', 27017)
    # Select the database
    db = client['mongoindex']
    # Select the Collections
    collection = db['zipstates']

    # Copy the .txt data to a List
    df = pd.read_csv("/Users/ouyang/Desktop/CSE7345PythonProgramming/week7/mysteryLatLong.txt")
    for i in df.loc[:]:
        mylist.append(float(i))

    # Store the longitude and latitude separately into two List
    for j in range(0, len(mylist)):
        if j%2!=0:
            tmplat.append(mylist[j])
        else:
            tmplong.append(mylist[j])
    # Establish a DataFrame for the output
    df2 = pd.DataFrame(columns=['Longitude', 'Latitude', '(cloest)City', 'State', 'Zipcode'])

    for p in range(0, len(tmplong)):
        # At the beginning, clear the distance[] list
        distance = []
        result = collection.find({}, {'city': 1, 'longitude': 1, 'latitude': 1, '_id': 0, 'zip_code':1, 'state':1})
        for q in result:
            tmpdict = {}
            tmpdict = q
            longi = tmpdict.get("longitude")
            lati = tmpdict.get("latitude")
            cit = tmpdict.get("city")
            stat = tmpdict.get("state")
            zico = tmpdict.get("zip_code")

            # Get rid of the NULL data and calculate the minimum distance
            # Select the cloest city information and put them into dictionary
            if longi != None:
                km = calculateDist(longi, lati, tmplong[p], tmplat[p])
                distance.append(km)
                if km == min(distance):
                    minDict['longitude'] = tmplong[p]
                    minDict['latitude'] = tmplat[p]
                    minDict['city'] = cit
                    minDict['zipcode'] = zico
                    minDict['state'] = stat

        # Use the append() method to add data into df2
        df3 = pd.DataFrame([[minDict.get('longitude'), minDict.get('latitude'), minDict.get('city'), minDict.get('state'), minDict.get('zipcode')]],
                           columns=['Longitude', 'Latitude', '(cloest)City', 'State', 'Zipcode'])
        df2 = df2.append(df3)
    print(df2)


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


if __name__ == "__main__":
    # createDatabase()
    # insertData()
    # acessData()
    # searchdb()
    # func_Explain_NoIndex()
    # func_Explain_Index()
    # print(totalDocs_NoIndex)
    # print(execTime_NoIndex)
    # plot_totalDocsExam()
    # plot_exeTime()
    # find_city_BaseOnZipcodes()
    find_CloestCity()
