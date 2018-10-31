from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4
import ssl
import urllib


context = ssl._create_unverified_context()
f = urllib.request.urlopen("https://www.dart.org", context=context).read()
s = str(f, encoding='utf-8')

bs = BeautifulSoup(s, 'html.parser')
# First layer
myul = bs.find("ul", {"class":"rideralerts"})
print(myul)