import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('SPY.histdata.csv', parse_dates = ['Date'])
df2 = df.sort_values(by=['Date'], ascending = True)
# print(df2)
# Drop the NaN rows
df2['MA100'] = df2['SPY'].rolling(100).mean()
df3 = df2.dropna()

money_bh = 1000.00
tmp_moneybh = []
holdingFraction_bh = 0.00

def buyhold():
    # j = 0
    money_bh = 1000.00
    tmp_moneybh = []
    holdingFraction_bh = 0.00
    for i in range(0, 4602):
        j = 4602-i
        if money_bh>0:
            if df3.loc[j,'SPY']>df3.loc[j,'MA100']:
                holdingFraction_bh = money_bh/df3.loc[j,'SPY'] + holdingFraction_bh
                money_bh = 0.00
                tmp_moneybh.append(money_bh)
                break
    print(holdingFraction_bh)
    for i in range(0,4602):
        if df3.loc[i,'SPY']<df3.loc[i,'MA100']:
            money_bh = holdingFraction_bh * df3.loc[i,'SPY']
            holdingFraction_bh = 0.00
            print(df3.loc[i,'SPY'])
            break
    print(money_bh)
# buyhold()

def buyhold1():
    # j = 0
    money_bh = 1000.00
    tmp_moneybh = []
    holdingFraction_bh = 0.00
    tmphold = []
    for i in range(0, 4602):
        j = 4602-i
        if df2.loc[j,'SPY']>df2.loc[j,'MA100']:
            if money_bh>0.01:
                holdingFraction_bh = money_bh/df2.loc[j,'SPY'] + holdingFraction_bh
                money_bh = 0.00
                tmp_moneybh.append(money_bh)
                tmphold.append(holdingFraction_bh)
                break
#     # print(holdingFraction_bh)
    for i in range(0,4602):
        if df2.loc[i,'SPY']<df2.loc[i,'MA100']:
            money_bh = holdingFraction_bh * df2.loc[i,'SPY']
            holdingFraction_bh = 0.00
            tmphold.append(df2.loc[i,'SPY'])
            break
    return money_bh
print(buyhold1())