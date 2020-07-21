'''
문제 이름 : 스타트링크
문제 번호 : 14889
풀이 일자 : 2020.07.21
'''
import sys, math
from itertools import combinations

n = int(sys.stdin.readline().strip())
answer = math.inf

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
combiLst = list(combinations([i for i in range(1, n+1)], n // 2))

for i in range(len(combiLst) // 2):
    startPoint = 0
    linkPoint = 0
    startTeam = combiLst[i]
    for j in range(n//2):
        current = startTeam[j]
        for k in startTeam :
            startPoint += board[current-1][k-1]
    linkTeam = combiLst[-i-1]
    for j in range(n//2):
        current = linkTeam[j]
        for k in linkTeam :
            linkPoint += board[current-1][k-1]
    answer = min(answer, abs(startPoint - linkPoint))
print(answer)