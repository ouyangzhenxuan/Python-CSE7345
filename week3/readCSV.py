import csv
import json

with open('worldcup.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    wcyears = []
    wcdates = []
    wclocation = []
    wcfirst = []
    wcsecond = []
    wcthird = []
    wcfourth = []
    wcgoalsScored = []
    wcmatchesPlayed = []
    wcattendence = []

    for row in readCSV:
        date = row[0]
        year = row[1]
        location = row[2]
        first = row[3]
        second = row[4]
        third = row[5]
        fourth = row[6]
        goalsScored = row[7]
        matchesPlayed = row[8]
        attendence = row[9]

        wcdates.append(date)
        wcyears.append(year)
        wclocation.append(location)
        wcfirst.append(first)
        wcsecond.append(second)
        wcthird.append(third)
        wcfourth.append(fourth)
        wcgoalsScored.append(goalsScored)
        wcmatchesPlayed.append(matchesPlayed)
        wcattendence.append(attendence)
    # print(wcdates)
    # print(wcgoalsScored)
    mylist = []
    for i in range(1, len(wcdates)):
        mylist.append(dict([(wcdates[0], wcdates[i]),(wcyears[0],wcyears[i]),
                        (wclocation[0],wclocation[i]),(wcfirst[0],wcfirst[i]),
                        (wcsecond[0],wcsecond[i]),(wcthird[0],wcthird[i]),
                        (wcfourth[0],wcfourth[i]),(wcgoalsScored[0],wcgoalsScored[i]),
                        (wcmatchesPlayed[0],wcmatchesPlayed[i]),(wcattendence[0],wcattendence[i])]))
    mylist2 = json.dumps(mylist, indent=4)
    tmpstr = mylist[3]["goalsScored"]
    mylist3 = []
    for j in range(0,5):
        tmp_date = mylist[0]["WorldCup"]
        tmp_bigNumGoal = mylist[0]["goalsScored"]
        tmp_dic = {}
        tmp_index = 0

        for i in range(0, len(mylist)):
            if int(tmp_bigNumGoal) < int(mylist[i]["goalsScored"]):
                tmp_bigNumGoal = mylist[i]["goalsScored"]
                tmp_dic = mylist[i]
                tmp_index = i
        mylist3.append(tmp_dic)
        mylist.pop(tmp_index)
        # print(mylist3)
    # print(mylist3)
    my_json1 = json.dumps(mylist3, indent=4)
    print("\nThere are top 5 greatest goalsScored below:")
    print(my_json1)

# WorldCup,year,location,first,second,third,fourth,goalsScored,matchesPlayed,attendance