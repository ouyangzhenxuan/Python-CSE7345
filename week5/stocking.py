import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('SPY.histdata.csv', parse_dates = ['Date'])
df2 = df.sort_values(by=['Date'], ascending = True)
# print(df2)
# Drop the NaN rows
df2['MA100'] = df2['SPY'].rolling(100).mean()
df3 = df2.dropna()
# print(df3)

tmpdata = []
money = 1000.00
tmpmoney = []
holdingFraction = 0.00

for i in range(0, 4602):
    j = 4602 - i
    # BUY
    if df3.loc[j, 'SPY'] > df3.loc[j, 'MA100']:
        tmpdata.append(df3.loc[j, 'SPY'])
        if money > 0.01:
            # Set a temp variavle to record the holdingFraction, and use the tmpholding to calculate the money
            #             tmpholding = holdingFraction
            holdingFraction = money / df3.loc[j, 'SPY'] + holdingFraction
            # money = money - holdingFraction * df3.loc[j, 'SPY']
            money = 0.00
            tmpmoney.append(money)
            tmpdata = []
            tmpholding = 0
        else:
            tmpmoney.append(money)
    # SELL
    else:
        if holdingFraction > 0.01:
            tmpdata.append(df3.loc[j, 'SPY'])
            money = holdingFraction * df3.loc[j, 'SPY'] + money
            tmpmoney.append(money)
            holdingFraction = 0
        else:
            tmpmoney.append(money)
#     tmpmoney.append(money)

# holdingFraction
print(tmpmoney)
print(holdingFraction)
print(money)
# tmpmoney[len(tmpmoney)-1]
# money
# df4 = df2.iloc[range(4502,4602)]
# # print(df4)
# a = df4.plot(y=['SPY','MA100'],x='Date')
# plt.plot(y=['SPY','MA100'],x='Date')
# plt.show()