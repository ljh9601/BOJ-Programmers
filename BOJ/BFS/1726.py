# 풀이일자 : 2020/05/07
# 문제 이름 : 로봇
# 문제 번호 : 1726
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 로봇을 원하는 위치로 이동시키고, 원하는 방향으로 바라보도록 하는데 필요한 최소 명령 횟수

import sys
from collections import deque

dx = [0, 0, 1 ,-1]
dy = [1, -1, 0, 0]

def right(x, y, direction) :
    if direction == 1 :
        nDir = 3
    if direction == 2 :
        nDir = 4
    if direction == 3 :
        nDir = 2
    if direction == 4 :
        nDir = 1
    if not visited[x][y][nDir]:
        visited[x][y][nDir] = visited[x][y][direction] + 1
        q.append((x, y, nDir))

def left(x, y, direction) :
    if direction == 1 :
        nDir = 4
    if direction == 2 :
        nDir = 3
    if direction == 3 :
        nDir = 1
    if direction == 4 :
        nDir = 2
    if not visited[x][y][nDir]:
        visited[x][y][nDir] = visited[x][y][direction] + 1
        q.append((x, y, nDir))

def move(x, y, curDir):
    nx = x 
    ny = y
    for _ in range(3):
        nx += dx[curDir-1]
        ny += dy[curDir-1]
        if nx <= 0 or ny <= 0 or nx > m or ny > n or board[nx][ny]:
            return
        if not visited[nx][ny][curDir]:
            visited[nx][ny][curDir] = visited[x][y][curDir] + 1
            q.append((nx, ny, curDir))

def bfs(start):
    q.append(start)
    visited[start[0]][start[1]][start[2]] = 1
    while q :
        x, y, currentDir = q.popleft()
        if x == endPos[0] and y == endPos[1] and currentDir == endPos[2]:
            return visited[x][y][currentDir] - 1
        right(x, y, currentDir)
        left(x, y, currentDir)
        nx = x + dx[currentDir-1]
        ny = y + dy[currentDir-1]
        if 0 < nx <= m and 0 < ny <= n:
            if not board[nx][ny] :
                move(x, y, currentDir)
        else:
            left(x, y, currentDir)
            right(x, y, currentDir)

m, n = map(int, sys.stdin.readline().strip().split())
board = [[0] * (n+1) for _ in range(m+1)]
q = deque()
for i in range(1, m+1):
    board[i][1:] = list(map(int, sys.stdin.readline().strip().split()))
visited = [[[0] * 5 for _ in range(n+1)] for __ in range(m+1)]
startPos = list(map(int, sys.stdin.readline().strip().split()))
endPos = list(map(int, sys.stdin.readline().strip().split()))
print(bfs(startPos))