'''
풀이일자 : 2020/05/10
문제 이름 : 양
문제 번호 : 3184
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : BFS
살아남은 양과 늑대의 수
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(posX, posY) :
    q = deque()
    q.appendleft((posX, posY))
    visited[posX][posY] = 1
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if not visited[nx][nx] :
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

r, c = map(int, sys.stdin.readline().strip().split())
board = ['0'] * c for _ in range(r)
visited = [0] * c for _ in range(r)
sheep = []
wolf = []
for i in range(r) :
    board[i] = list(map(str, sys.stdin.readline().strip()))
    for j in range(c):
        if board[i][j] == 'o' :
            sheep.append((i,j))
        if board[i][j] == 'v' :
            wolf.append((i,j))
for i in range(r):
    for j in range(c):
        bfs(i, j)