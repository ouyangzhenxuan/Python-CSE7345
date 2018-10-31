# Basic Python Quest
# When returning lists of values, order is not important unless specified

__STUDENT_ID__  = "47784546"     # replace with your 8 digit student id
__CODING_NAME__ = "Starving"        # replace with your coding name -


def compare(a, b):
    return a <= b;

def isSorted(list):
    """ return boolean depending on if list sorted
    >>> isSorted([2,4,7,7,99,122]) -> True
    >>> isSorted(['a','b','c'])  -> True
    >>> isSorted(['a','z','b','c'])  -> False
    constraint: MAY NOT USE: sorted( ) function or sort library
    """
    for index, item in enumerate(list[1:len(list)]):
        if compare(list[index], item) is False:  # 用listtest[0]和listtest[1]比较
            return False  # 当后者比前者大不成立的时候，返回False，结束程序
    return True


def sortAndUnique(a, b):
    if a < b:
        return True
    else:
        return False
    
def isSortedAndUnique(list):
    """ return boolean depending on if list sorted
    >>> isSortedAndUnique([2,4,7,7,99,122]) -> False
    >>> isSortedAndUnique(['a','b','c'])  -> True
    >>> isSortedAndUnique(['a','z','b','b','c'])  -> False
    constraint: MAY NOT USE: set
    """
    for index, item in enumerate(list[1:len(list)]):
        if sortAndUnique(list[index], item) is False:  # 用listtest[0]和listtest[1]比较
            return False  # 当后者比前者大不成立的时候，返回False，结束程序
    return True


def uniValues(a, b):
    if a == b:
        return False
    return True


def hasUniqueValues(list):
    """ return boolean depending on if list has unique values
    >>> hasUniqueValues([2,4,7,99,122,7]) -> False
    >>> hasUniqueValues(['a','b','c'])  -> True
    >>> hasUniqueValues(['a','z','b','b','c'])  -> False
    constraint: MAY NOT USE: set
    """
    for i, item in enumerate(list):
        for j, jtem in enumerate(list[i+1:]):
            if uniValues(item, jtem) is False:
                return False

    return True


def isEqual(a, b):
    return  a==b;

def genSortedArrayUniqueValues(list):
    """ return sorted version of list without duplicates
    >>> genSortedArrayUniqueValues([2,4,7,7,122,99]) -> [2,4,7,99,122]
    >>> genSortedArrayUniqueValues(['a','b','z','c', 'a'])  -> ['a','b','c','z']
    constraint: MAY NOT USE: set
    """
    tmpList = sorted(list)
    for index, item in enumerate(tmpList[1:]):
        if isEqual(tmpList[index], item) is True:
            del_i = index
    del tmpList[del_i]
    return tmpList


def listToMapTwoByTwo(list):
    """ return a map based on the order of list elements.
    >>> listToMapTwoByTwo(['foo','bar'])     ->  {"foo":"bar"}
    >>> listToMapTwoByTwo(['a',2, 3,'foo'])  ->  {"a":2,3:'foo'}
    >>> listToMapTwoByTwo([])  -> {}
    """
    myDict = {}  # 键值对，在python里面叫字典
    for index in range(0, len(list), 2):
        myDict[list[index]] = list[index + 1]

    return myDict


def wordsInStringToDictWordCount(s):
    """ return a dict of words in string and count
    >>> wordsInStringToDictWordCount('foo bar   bar') -> {'foo':1, 'bar':2}
    >>> wordsInStringToDictWordCount('') -> {}
    constraint: MAY NOT USE: Counter
    """
    myDict = {}
    tmpList = s.split(" ")
    for key1 in tmpList:
        myDict[key1] = myDict.get(key1, 0) + 1
    myDict.pop("", 0)
    return myDict


import  copy
def reverseWordsInString(string):
    """ return a string with words reversed with one space separators
    >>> reverseWordsInString('foo bar bar baz') -> 'baz bar bar foo'
    constraint: MAY NOT USE: list.reverse()
    """
    tmpList1 = string.split(" ")
    tmpList2 = copy.deepcopy(tmpList1)
    for i in range(len(tmpList1) - 1):
        tmpItem = tmpList2[i]
        tmpList2[i] = tmpList1[len(tmpList1) - i - 1]
        tmpList2[len(tmpList1) - i - 1] = tmpItem
    string2 = " ".join(tmpList2)  # join函数是用来在list的每两个元素中加入一个特定的符号，转换成字符串
    # print(string2)
    return string2


def genListOfOverlaps(list1, list2):
    """ return list of values appearing in both lists
    >>> genListOfOverlaps([2,4,6,8],[6,2,2,9,7]) -> [2,6]
    >>> genListOfOverlaps([2,4,6,8],[2,4,6,8]) -> [2,4,6,8]
    >>> genListOfOverlaps([2,4,6,8],[1,1,9,7]) -> []
    """
    tmpList = []
    for item in list1:
        if item in list2:
            tmpList.append(item)
    tmpList = sorted(tmpList)
    tmpList2 = []
    for item in tmpList:
        if not item in tmpList2:
            tmpList2.append(item)
    return tmpList2


def removeDupsNoSet(list):
    """ remove duplicates in the list without using Python Set
    >>> removeDupsNoSet([1,1,2,2,5,6]) -> [1,2,5,6]
    constraint: MAY NOT USE: set
    """
    tmpList = []
    for item in list:
        if not item in tmpList:
            tmpList.append(item)
    # print(tmpList)
    return tmpList


def removeDupsUseSet(list1):
    """ remove duplicates in the list  using Python Set
    >>> removeDupsUseSet([1,1,2,2,5,6]) -> [1,2,5,6]
    constraint: MUST USE: set
    """
    return list(set(list1))


if __name__ == '__main__':
    #write your own test code here
    print('im starving!!!')
    print ('ready to go')