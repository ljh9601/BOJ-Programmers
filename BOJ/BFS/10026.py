# 풀이일자 : 2020/04/09
# 문제 이름 : 적록색약
# 문제 번호 : 10026
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 적록색맹인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수
import sys
from collections import deque
sectorCnt = 0
sectorCntForRG = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(posX, posY, current):
    global sectorCnt
    visited[posX][posY] = True
    sectorCnt += 1
    q = deque()
    q.appendleft((posX, posY))
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if board[nx][ny] == current and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.appendleft((nx, ny))

def bfsForRG(posX, posY, current):
    global sectorCntForRG
    visitedForRG[posX][posY] = True
    sectorCntForRG += 1
    q = deque()
    q.appendleft((posX, posY))
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if boardForRG[nx][ny] == current and not visitedForRG[nx][ny]:
                    visitedForRG[nx][ny] = True
                    q.appendleft((nx, ny))

n = int(sys.stdin.readline().strip())
board = [sys.stdin.readline().strip() for i in range(n)]
boardForRG = [['0'] * n for i in range(n)]
for i in range(n):
    boardForRG[i] = board[i].replace('G', 'R')

visited = [[False] * n for i in range(n)]
visitedForRG = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] :
            bfs(i, j, board[i][j])
        if not visitedForRG[i][j]:
            bfsForRG(i, j, boardForRG[i][j])
print('{0} {1}'.format(sectorCnt, sectorCntForRG))