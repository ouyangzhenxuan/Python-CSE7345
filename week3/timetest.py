file = open("/Users/ouyang/Desktop/longstr2.txt",'r')
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
# print(myDict)
import re,collections
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

print(wordsInStringToDictWordCount4())
