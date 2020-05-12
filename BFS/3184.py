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

def bfs(start) :
    q = deque()
    q.appendleft(start)
    visited[start[0]][start[1]] = True
    countSheep = 0
    countWolf = 0
    if board[start[0]][start[1]] == 'o' :
        countSheep += 1
    else :
        countWolf += 1
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if not visited[nx][ny] and board[nx][ny] != '#':
                    if board[nx][ny] == 'o' :
                        countSheep += 1
                    if board[nx][ny] == 'v' :
                        countWolf += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return (countSheep, 0) if countSheep > countWolf else (0, countWolf)

r, c = map(int, sys.stdin.readline().strip().split())
visited = [[False] * c for _ in range(r)]
ansSheep = 0
ansWolf = 0
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
for i in range(r) :
    for j in range(c) :
        if not visited[i][j] and (board[i][j] =='o' or  board[i][j] == 'v'):
            result = bfs((i, j))
            ansSheep += result[0]
            ansWolf += result[1]
print('{0} {1}'.format(ansSheep, ansWolf))