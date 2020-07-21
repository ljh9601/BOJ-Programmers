'''
문제 이름 : 치킨 배달
문제 번호 : 15686
풀이 일자 : 2020.07.21
'''
import sys, math
from itertools import combinations

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
chicken = []
home = []
combiLst = []
answer = math.inf
for i in range(n):
    for j in range(n):
        if board[i][j] == 2 :
            chicken.append((i, j))
        elif board[i][j] == 1 :
            home.append((i, j))
indexLst = [i for i in range(len(chicken))]
for i in range(1, m+1):
    combiLst.extend(list(combinations(indexLst, i)))
for combi in combiLst :
    minDists = []
    tempChicken = []
    for values in combi :
        tempChicken.append(chicken[values])
    for (x, y) in home :
        dists = []
        for (xP, yP) in tempChicken :
            dists.append(abs(x - xP) + abs(y - yP))
        minDist = min(dists)
        minDists.append(minDist)
    answer = min(answer, sum(minDists))
print(answer)