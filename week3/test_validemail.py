import re, pytest, os
import validemail as Reg

def getTotalTestCount():
    f = open(os.path.basename(__file__), 'r')
    lines = f.read()
    resList = re.findall(r'^def test_', lines, re.M)
    return len(resList)

def init():
    # get test & user-specific info  --------------
    tt   = getTotalTestCount()
    id   = Reg.__STUDENT_ID__
    name = Reg.__QUEST_NAME__
    cat  = 'Reg'
    return (id,name,cat,tt)


def test_is_validemail2_true_1():
    assert Reg.is_validemail2('simple@example.com') == True

def test_is_validemail2_true_2():
    assert Reg.is_validemail2('very.common@example.com') == True

def test_is_validemail2_true_3():
    assert Reg.is_validemail2('disposable.style.email.with+symbol@example.com') == True

def test_is_validemail2_true_4():
    assert Reg.is_validemail2('"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com') == True

def test_is_validemail2_true_5():
    assert Reg.is_validemail2('example-indeed@strange-example.com') == True

def test_is_validemail2_true_6():
    assert Reg.is_validemail2('#!$%&\'*+-/=?^_`{}|~@example.org') == True

def test_is_validemail2_true_7():
    assert Reg.is_validemail2('"()<>[]:,;@\\\"!#$%&\'-/=?^_`{}| ~.a"@example.org') == True

def test_is_validemail2_true_8():
    assert Reg.is_validemail2('john..doe@example.com') == True

def test_is_validemail2_false_1():#
    assert Reg.is_validemail2('Abc.example.com') == True

def test_is_validemail2_false_2():
    assert Reg.is_validemail2('Abc.example@qcw_.com') == True

def test_is_validemail2_false_3():
    assert Reg.is_validemail2('..awe.45@mail.com') == True

def test_is_validemail2_false_4():#
    assert Reg.is_validemail2('.abd.qwe@example.com') == True

def test_is_validemail2_false_5():#
    assert Reg.is_validemail2('Abc.example@_qcc.com') == True

def test_is_validemail2_false_6():#
    assert Reg.is_validemail2('Abc.example.@qcc.com') == True




