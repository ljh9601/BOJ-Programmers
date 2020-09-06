import sys
from itertools import permutations
from collections import defaultdict
from copy import deepcopy

# 입력
red, green, blue = map(int, sys.stdin.readline().strip().split()) 
string = sys.stdin.readline().strip()
if len(string) < 3 :
    if len(set(string)) == 1 :
        if string[0] == 'R':
            print(min(green, blue), 1)
        elif string[0] == 'G':
            print(min(red, blue), 1)
        elif string[0] == 'B':
            print(min(red, green), 1)
        sys.exit()

flowers = ['R','G','B']
countDic = defaultdict(int)
countDic['R'] = string.count('R')
countDic['G'] = string.count('G')
countDic['B'] = string.count('B')

combis = list(permutations(flowers, 3))
allStrings = []
for a,b,c in combis :
    allStrings.append((a+b+c) * (len(string)//3 + 1))
ans = []
for combiStr in allStrings :
    cost, cnt = 0, 0
    cntDic = deepcopy(countDic)
    for i in range(len(string)):
        cntDic[string[i]] -= 1
        if string[i] == combiStr[i] :
            continue
        else :
            if cntDic[combiStr[i]] > 0 :
                cntDic[combiStr[i]] -= 1
                cntDic[string[i]] += 1
            else :
                if combiStr[i] == 'R':
                    cost += red
                elif combiStr[i] == 'G':
                    cost += green
                else :
                    cost += blue
                cntDic[string[i]] += 1
            cnt += 1
    ans.append([cost, cnt])
ans = sorted(ans, key = lambda x : (x[0], x[1]))
print(ans[0][0], ans[0][1])