import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4
import ssl
import urllib

# Get the whole html code of the website
context = ssl._create_unverified_context()
f = urllib.request.urlopen("http://www.pythonscraping.com/pages/page3.html", context=context).read()
s = str(f, encoding='utf-8')
# print(s)

bs = BeautifulSoup(s, 'html.parser')
# First layer
mytable = bs.find('table', {'id':'giftList'})
# print(mytable)

# childList is the children list of mytable
childList = list(mytable.children)
# print(childList)
# print(len(childList))

# childList2 is the children list of mytable with bs4's element
childList2 = [x for x in childList if type(x)==bs4.element.Tag]
# print(childList2)

for child in childList2:
    mytd = child.find_all('td')
    # print(mytd)
    if(len(mytd)>0):
        print(mytd[0].getText().strip('\n'))
