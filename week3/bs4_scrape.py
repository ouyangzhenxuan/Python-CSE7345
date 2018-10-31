import bs4
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import re

context = ssl._create_unverified_context()
f = urllib.request.urlopen("https://www.nasdaq.com/quotes/stock-quotes.aspx", context=context).read()
s = str(f, encoding='utf-8')
# print(str(f, encoding='utf-8'))
bs = BeautifulSoup(s, 'html.parser')
mytable = bs.find('div', {'class':'genTable marginL15px'})
myconame = bs.find_all('div', {'class':'coName small'})

itemList = []
trendList2 = []
volumeList = []
volumeList2 = []
tmpList = []

for child in mytable.children:
    if (type(child) is bs4.element.Tag):
        tblist = child.find_all('tbody')
        for child2 in child.children:
            if (type(child2) is bs4.element.Tag):
                trlist = child2.find_all('tr')
                for child3 in child2.children:
                    if(type(child3) is bs4.element.Tag):
                        tdlist = child3.find_all("td")
                        for child4 in child3.children:
                            if (type(child4) is bs4.element.Tag):
                                tdivlist = child4.find_all('div')
                                if (len(tdivlist) > 0):
                                    itemList.append(tdivlist[1].getText().strip('\n'))
                        if (len(tdlist) > 0):
                            tmpList.append(tdlist[2].getText().strip('\n'))
                            volumeList.append(tdlist[3].getText().strip('\n'))

for i in range(0, len(volumeList)):
    volumeList2.append(str(volumeList[i]).replace(',','').replace(' ',''))

for i in range(0, len(tmpList)):
    if str(tmpList[i]).__contains__('▲'):
        trendList2.append((re.findall(r'(\d+\.\d\d)?%', tmpList[i]))[0])
    if str(tmpList[i]).__contains__('▼'):
        trendList2.append('-'+(re.findall(r'(\d+\.\d\d)?%', tmpList[i]))[0])


import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
x = itemList
x_short = []
for i in range(len(x)):
    xx = (x[i].split(' '))[0]
    x_short.append(xx)
pct = []
for i in range(len(volumeList2)):
    pct.append(float(volumeList2[i]))
x_pos = [i for i, _ in enumerate(x_short)]
plt.bar(x_pos, pct, color = 'red')
plt.xticks(x_pos, x_short)
plt.xlabel("company")
plt.ylabel("Volume")
plt.title('Most Active September 7, 2018')
plt.show()

plt.style.use('ggplot')
x = itemList
x_short = []
for i in range(len(x)):
    xx = (x[i].split(' '))[0]
    x_short.append(xx)
pct = []
for i in range(len(trendList2)):
    pct.append(float(trendList2[i]))
x_pos = [i for i, _ in enumerate(x_short)]
plt.bar(x_pos, pct, color = 'green')
plt.xticks(x_pos, x_short)
plt.xlabel("Company")
plt.ylabel("pct change")
plt.title('Percent Change September 7, 2018')
plt.show()



