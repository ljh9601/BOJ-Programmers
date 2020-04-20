# 풀이일자 : 2020/04/19
# 문제 이름 : 섬의 개수
# 문제 번호 : 4963
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS, 그래프 이론
# 섬의 개수를 구하라

import sys
from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]
count = 0

def bfs(posX, posY):
    global count
    queue = deque()
    count += 1
    queue.appendleft((posX, posY))
    while queue :
        x, y = queue.popleft() # queue는 비어있다.
        board[x][y] = 0
        #visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w :
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    queue.append((nx, ny))
                    
while True :
    w, h = map(int, sys.stdin.readline().strip().split())
    if not w and not h :
        exit()
    count = 0
    #visited = [[False] * w for _ in range(h)]
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                bfs(i, j)
    print(count)