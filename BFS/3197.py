'''
풀이일자 : 2020/05/22
문제 이름 : 백조의 호수
문제 번호 : 3197
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : BFS
두마리의 백조가 만날 수 있는 일수
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs() :
    while q :
        x, y = q.popleft()
        if x == swan[1][0] and y == swan[1][1] :
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if not visited[nx][ny] :
                    if board[nx][ny] == '.' :
                        q.append((nx, ny))
                    else :
                        qNext.append((nx, ny))
                visited[nx][ny] = True
    return False

def melt():
    while waterQ :
        x, y = waterQ.popleft()
        if board[x][y] == 'X' :
            board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if not visitedWater[nx][ny] :
                    visitedWater[nx][ny] = True
                    if board[nx][ny] == 'X' :
                        waterNext.append((nx, ny))
                    else :
                        waterQ.append((nx, ny))

r, c = map(int, sys.stdin.readline().strip().split())
board = [['0'] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
visitedWater = [[False] * c for _ in range(r)]
swan = []
q = deque()
qNext = deque()
waterQ = deque()
waterNext = deque()
cnt = 0
for i in range(r):
    board[i] = list(map(str, sys.stdin.readline().strip()))
    for j in range(c):
        if board[i][j] == '.' :
            waterQ.append((i, j))
            visitedWater[i][j] = 1
        elif board[i][j] == 'L' :
            waterQ.append((i, j))
            swan.append((i, j))
            board[i][j] = '.'
visited[swan[0][0]][swan[0][1]] = True
q.append((swan[0][0], swan[0][1]))
while True :
    melt()
    if bfs() :
        print(cnt)
        break
    else :
        q = qNext
        waterQ = waterNext
        qNext = deque()
        waterNext = deque()
        cnt += 1