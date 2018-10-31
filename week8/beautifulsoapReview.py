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
f = urllib.request.urlopen("https://www.nasdaq.com/symbol/nvda/dividend-history", context=context).read()
s = str(f, encoding='utf-8')

bs = BeautifulSoup(s, 'html.parser')
# First layer
mydiv = bs.find("div", {"class":"genTable"})
# print(mydiv)

for child in mydiv.children:
    if(type(child) is bs4.element.Tag):
        mytbody = child.find_all("tbody")
        # print(mytbody)
        for child2 in child.children:
            if(type(child2) is bs4.element.Tag):
                mytr = child2.find_all("tr")
                # print(mytr)
                for child3 in child2.children:
                    if(type(child3) is bs4.element.Tag):
                        mytd = child3.find_all("td")
                        # print(mytd)
                        for child4 in child3.children:
                            if(type(child4) is bs4.element.Tag):
                                myDeclDate = child4.find_all("span", {"id":"quotes_content_left_dividendhistoryGrid_DeclDate_0"})
                                # print(myDeclDate)
                                if(len(myDeclDate) > 0):
                                    # print(myDeclDate)
                                    print(myDeclDate[0].getText().strip("\n"))

myLastSale = bs.find("div", {"id":"qwidget_lastsale"})
print(myLastSale.getText())

mydiv3 = bs.find("div", {"class":"rail-module"})
# print(mydiv3)
for child in mydiv3.children:
    if(type(child) is bs4.element.Tag):
        myli = child.find_all("li")
        # print(myli)
        # if(len(myli)>0):
            # print(myli[0].getText().strip("\n"))
        for child2 in child:
            if(type(child2) is bs4.element.Tag):
                myspan = child2.find_all("span")
                # print(myspan)
                if(len(myli)>0):
                    print(myspan[0].getText().strip())

mydiv5 = bs.find_all("div", {"class":"rail-module"})
headlineLinks = mydiv5[0].find_all("a")
# print(headlineLinks)
for child in headlineLinks:
    print(child.getText().strip())

mydiv4 = bs.find("div", {"id":"RailIndexTable"})
# print()