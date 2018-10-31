import re

__STUDENT_ID__  = "47784546"        # replace with your 8 digit student id
__CODING_NAME__ = "Starving2"           # replace with your coding name - max 15 characters
__QUEST_NAME__ = "imgood"  # to meet the requirement of testFile

def is_validemail2(string):
    if (re.match(r'[^\.](\w|\d|\.|[~!#@$%^&*()_+{}|:"<>?=;,/` ]|\\|\-|(\')|(\[)|(\]))*[^\.]@[^\_](\w|\d|\_|\-)*[^\_]\.\w+',
               string)) is not None:
        return True
    return False




# def is_validemail(string):
#     # four part: local, the '@' symbol, domain1, domain2
#     if string.__contains__('@'):
#         print('this address has a @ ')
#         addList = string.split('@')
#         if string[0]=='.':
#             print("the first letter cannot be '.'")
#             return False
#
#         local = addList[0]
#         domain = addList[1]
#
#         # print(addList)
#     else:
#         print('Not a valid email address')
#     return True