# 풀이일자 : 2020/04/30
# 문제 이름 : 맥주 마시면서 걸어가기
# 문제 번호 : 9205
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(posX, posY):
    stack = deque()
    visited = []
    stack.append([posX, posY, 20])
    visited.append([posX, posY, 20])
    while stack :
        x, y, left = stack.pop()
        if x == endX and y == endY :
            return 'happy'
        for nPosX, nPosY in cs :
            if [nPosX, nPosY, 20] not in visited :
                dist = abs(nPosX - x) + abs(nPosY - y)
                if left * 50 >= dist :
                    visited.append([nPosX, nPosY, 20])
                    stack.append([nPosX, nPosY, 20])
    return 'sad'

tcNum = int(sys.stdin.readline().strip())
for _ in range(tcNum):
    csNum = int(sys.stdin.readline().strip())
    startX, startY = map(int, sys.stdin.readline().strip().split())
    cs = deque()
    for i in range(csNum) :
        cs.append(list(map(int, sys.stdin.readline().strip().split())))
    endX, endY = map(int, sys.stdin.readline().strip().split())
    cs.append([endX, endY])
    print(dfs(startX, startY))