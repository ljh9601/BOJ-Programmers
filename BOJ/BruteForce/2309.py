'''
문제 이름 : 선분 그룹
문제 번호 : 2309
풀이 일자 : 2020.07.20
'''
import sys
from itertools import combinations

small = []
for i in range(9):
    small.append(int(sys.stdin.readline().strip()))
smallCombis = list(combinations(small, 7))
for combi in smallCombis :
    sumVal = sum(combi)
    if sumVal == 100 :
        for c in sorted(combi) :
            print(c)
        sys.exit()