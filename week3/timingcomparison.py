import collections
import re
import timeit

def wordsInStringToDictWordCount(string):
    myDict = {}
    tmpList = string.split(" ")
    for key1 in tmpList:
        myDict[key1] = myDict.get(key1, 0) + 1
    myDict.pop("", 0)
    return myDict

def wordsInStringToDictWordCount2(string):
    w = re.findall(r'\w*',string)
    mydic = collections.Counter(w)
    mydic.pop('')
    return mydic

def wordsInStringToDictWordCount3():
    file = open("/Users/ouyang/Desktop/longstr2.txt", 'r')
    myDict = {}
    str = ''
    f = file.readlines()
    for i in range(len(f)):
        if f[i] != '\n':
            str += f[i]
    tmpList = str.split(" ")
    for key1 in tmpList:
        myDict[key1] = myDict.get(key1, 0) + 1
        myDict.pop("", 0)
    return myDict

def wordsInStringToDictWordCount4():
    file = open("/Users/ouyang/Desktop/longstr2.txt", 'r')
    str = ''
    f = file.readlines()
    for i in range(len(f)):
        if f[i] != '\n':
            str += f[i]
    w = re.findall(r'\w*',str)
    mydic = collections.Counter(w)
    mydic.pop('')
    return mydic

mytime1 = timeit.timeit('wordsInStringToDictWordCount("foo bar   bar")',
                       'from __main__ import wordsInStringToDictWordCount',
                       number=10 )
mytime2 = timeit.timeit('wordsInStringToDictWordCount2("foo bar   bar")',
                       'from __main__ import wordsInStringToDictWordCount2',
                       number=10 )
mytime3 = timeit.timeit('wordsInStringToDictWordCount3()',
                       'from __main__ import wordsInStringToDictWordCount3',
                       number=10 )
mytime4 = timeit.timeit('wordsInStringToDictWordCount4()',
                       'from __main__ import wordsInStringToDictWordCount4',
                       number=10 )

import matplotlib.pyplot as plt
plt.style.use('ggplot')
x = ['Not Counter', 'Counter']
x_pos = [i for i, _ in enumerate(x)]
pct = [mytime1, mytime2]
plt.bar(x_pos, pct, color = 'green')
plt.xticks(x_pos, x)
plt.ylabel("seconds")
plt.title('Time Comparison\n {foo bar bar}')
plt.show()

plt.style.use('ggplot')
x2 = ['Not Counter', 'Counter']
x_pos2 = [i for i, _ in enumerate(x2)]
pct = [mytime3, mytime4]
plt.bar(x_pos2, pct, color = 'red')
plt.xticks(x_pos2, x)
plt.ylabel("seconds")
plt.title('Time Comparison\n10000 words')
plt.show()


