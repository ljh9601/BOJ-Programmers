# 풀이일자 : 2020/04/29
# 문제 이름 : 불
# 문제 번호 : 5427
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 탈출이 가능한지에 대한 여부
# 불과 현재 나의 위치를 동시에 bfs 돌리면 된다.

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    q = deque()
    q.appendleft(start)
    visited[start[0]][start[1]] = 1
    while q :
        length = len(q)
        for ___ in range(length):
            currentX, currentY = q.popleft()
            for j in range(4):
                nx = currentX + dx[j]
                ny = currentY + dy[j]
                if 0 <= nx < h and 0 <= ny < w :
                    if not visited[nx][ny] and board[nx][ny] == '.' :
                        visited[nx][ny] = visited[currentX][currentY] + 1
                        q.append((nx, ny))
                elif nx < 0 or ny < 0 or nx >= h or ny >= w:
                    return visited[currentX][currentY]
        firebfs()
    return -1

def firebfs():
    lengt = len(fire)
    for ____ in range(lengt):
        currentFireX, currentFireY = fire.popleft()
        for i in range(4):
            nFireX = currentFireX + dx[i]
            nFireY = currentFireY + dy[i]
            if 0 <= nFireX < h and 0 <= nFireY < w :
                if board[nFireX][nFireY] == '.':
                    board[nFireX][nFireY] = '*'
                    fire.append((nFireX, nFireY))    

tcNum = int(sys.stdin.readline().strip())
result = []
for _ in range(tcNum):
    w, h = map(int, sys.stdin.readline().strip().split())
    board = [list(map(str, sys.stdin.readline().strip())) for ___ in range(h)]
    visited = [[0] * w for i in range(h)]
    fire = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@' :
                start = (i, j)
                board[i][j] = '.'
                continue
            if board[i][j] == '*' :
                fire.append((i,j))
                continue
    firebfs()
    ans = bfs(start)
    print(ans if ans > 0 else 'IMPOSSIBLE')