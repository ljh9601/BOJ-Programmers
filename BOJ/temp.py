import sys
import pandas
from collections import defaultdict

dt = pandas.read_csv("/Users/Janghaeng/Downloads/stock_data.csv")
df = pandas.DataFrame.from_dict(dt)
res = defaultdict()
df = dict(list(df.groupby('symbol')))

indexList = []
resultDict = defaultdict(dict)
for key in df.keys():
    res = defaultdict(list)
    if key not in indexList:
        indexList.append([key, list(df[key].index)[-1] + 1])
    for idx in df[key].index:
        tmp = [df[key]['date'][idx], df[key]['open'][idx]]
        res[key].append(tmp)
    resultDict[key] = res
print(resultDict['abuser'])
#print(res)