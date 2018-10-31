#Quest: Regex, Files, Urls

import re, pytest

__STUDENT_ID__  = "47784546"        # replace with your 8 digit student id
__CODING_NAME__ = "Starving2"           # replace with your coding name - max 15 characters
__QUEST_NAME__ = "imgood"  # to meet the requirement of testFile

def count_vowels(mystr):
    """return the number of vowels, upper and lowercase a,e,i,o,u in the string
    >>> count_vowels('aaacvemmikkOOzzuU')  -> 9
    """
    mylist = re.findall(r'[aeiou]|[AEIOU]', mystr)
    return len(mylist)

def is_valid_python_hex(mystr):
    """is string a valid hex: begins with 0x and contains only 0-9 and A-F (lower or upper)
     >>> is_valid_python_hex('0x1A2f') -> True
     >>> is_valid_python_hex('x1A2f')  -> False
     >>> is_valid_python_hex('0x1A2G') -> False
    """
    mylist = list(mystr)
    print(mylist)
    count = 0
    if (mylist[0] == '0') & (mylist[1] == 'x'):
        for i in range(2, len(mylist)):
            if (ord(mylist[i]) >= 48 and ord(mylist[i]) <= 57) or (ord(mylist[i]) >= 65 and ord(mylist[i]) <= 70) or (
                    ord(mylist[i]) >= 97 and ord(mylist[i]) <= 102):
                count += 1
    if count == len(mylist) - 2:
        return True
    return False

def has_vowel(mystr):
    """   return True if a vowel upper or lowercase in string
    >>> has_vowel("zcxvsd")     -> False
    >>> has_vowel("vcbxvefjk")  -> True
    """
    set1 = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    mylist = list(mystr)
    for i in range(len(mylist)):
        if ord(mylist[i]) in set1:
            return True
    return False

def is_integer(mystr):
    """ returns True if integer with optional minus sign
    >>> is_integer("2345")     -> True
    >>> is_integer("-192345")  -> True
    >>> is_integer("234x5")    -> False
    """
    mylist = list(mystr)
    set1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if (mylist[0] == '-') or (mylist[0] in set1):
        for i in range(1, len(mylist)):
            if mylist[i] not in set1:
                return False
        return True
    return False

def get_extension(mystr):
    """ returns the extension for a filename or 'NONE' if no extension
    >>> get_extension('foo.zip')     -> 'zip'
    >>> get_extension('foo.doc.txt') -> 'txt'
    >>> get_extension('foozip')      -> 'NONE'
    """
    if '.' in mystr:
        mylist = mystr.split(".")
        return mylist[len(mylist) - 1]
    return 'NONE'

def is_number(mystr):
    """ floating point number with optional - sign and optional decimal point
    >>> is_number('234')        -> True
    >>> is_number('-234')       -> True
    >>> is_number('234.')       -> True
    >>> is_number('234.999')    -> True
    >>> is_number('234.99.77')  -> False
    >>> is_number('234a.88')    -> False
    """
    try:
        number = float(mystr)
        return True
    except ValueError:
        return False

def convert_date_format(mystr):
    """ convert date format YYYY-MO-DAY  TO MO-DAY-YYYY. If not in date format
        return "NONE" . Check only 4 digits for year and 2 digits for MO and DAY
    >>> convert_date_format('2018-03-04')  -> '03-04-2018'
    >>> convert_date_format('2018.03-04')  -> 'NONE'
    >>> convert_date_format('2018-03-054') -> 'NONE'
    """
    if mystr.count('-',0,len(mystr))==2:
        mylist = mystr.split("-")
        tmplist = []
        # print(mylist[0].__len__())
        if mylist[0].__len__()==4 and mylist[1].__len__()==2 and mylist[2].__len__()==2:
            tmplist.append(mylist[1])
            tmplist.append(mylist[2])
            tmplist.append(mylist[0])
            tmpstr = "-".join(tmplist)
            return tmpstr
        return 'NONE'
    return 'NONE'



#File functions
def readFileCountLines(filename):
    """use download file from Canvas: pytestFile1.txt - return number of lines
    >>> readFileCountLines('pytestFile1.txt')  -> 4
    """
    f = open(filename, 'r')
    strFile = f.readlines()
    countNum = len(strFile)
    f.close()
    return countNum

def readFileCountStringOccurrences(filename, stringval):
    """read file: pyTestFile1.txt  - return number of times  stringval appears
    >>> readFileCountStringOccurrences('pytestFile1.txt','rollo')  -> 3
    """
    f = open(filename, 'r')
    strFile = f.readlines()
    countNum = 0
    for i in range(0, len(strFile)):
        tmplist = strFile[i].split()
        for j in tmplist:
            if j == stringval:
                countNum += 1
    f.close()
    return countNum

def readFileSumDigitsGreaterThanNumber(filename, number):
    """e.g. file = "hello22world2100and18and 1000", number =999 -> 3100
     >>> readFileSumDigitsGreaterThanNumber('pytestFile1.txt',15)  -> 88
    """
    f = open(filename, 'r')
    ff = f.read()
    sum1 = 0
    mylist1 = re.findall(r'\d*', ff)
    for i in range(0, len(mylist1)):
        try:
            tmpNum = int(mylist1[i])
            if tmpNum >= number:
                sum1 += tmpNum
        except:
            pass
    return sum1

def remove_all_but_alpha(mystr):
    """ remove all characters that are not alpha a-z A-Z
    >>> remove_all_but_alpha('hey-99-where8isthe**big_table**') -> 'heywhereisthebigtable'
    """
    mylist1 = re.findall(r'([a-z]|[A-Z])', mystr)
    str1 = ''
    for i in range(0, len(mylist1)):
        str1 = str1 + mylist1[i]
    return str1

#URL functions

import bs4
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import urlopen

def readurlCountStringOccurrences(urlname, stringval):
    """return number of times  stringval appears in text of url - ignore case
     >>> readurlCountStringOccurrences('http://s2.smu.edu/~coyle/testurls/foo.txt','rollo')  -> 3
    """
    content = urllib.request.urlopen(urlname).read();
    content1 = str(content, encoding="utf-8")
    mylist = re.findall(r'([Rr]ollo).*', content1)
    return mylist.__len__()

def readurlCountValidPhoneNumbers(urlname):
    """return count of valid phone number formats: no separator, dash separator, period separator:
    valid: 2126663333, 212-666-3333, 212.666.3333
    invalid: 212-444.5555, 212.333-4444, 212, 6363636363636
    >>> readurlCountValidPhoneNumbers('http://s2.smu.edu/~coyle/testurls/foo.txt')  -> 3
    """
    content = urllib.request.urlopen(urlname).read();
    content1 = str(content, encoding="utf-8")
    mylist = re.findall(r'\d\d\d-?\d\d\d-?\d\d\d\d', content1)
    mylist2 = re.findall(r'\d\d\d\.?\d\d\d\.?\d\d\d\d', content1)
    return len(set(mylist + mylist2))



if __name__  == '__main__':
    print ("Im starving week2")
    print ("To test your code execute: python test_QuestFilesUrls.py  or on command line execute: pytest ")



