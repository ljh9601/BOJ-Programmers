'''
풀이일자 : 2020/05/16
문제 이름 : 달이 차오른다, 가자.
문제 번호 : 1194
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : BFS
민식이가 미로를 탈출하는데 걸리는 최소 이동 횟수
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start) :
    q = deque()
    visited[start[0]][start[1]][start[2]] = 1
    q.appendleft(start)
    while q :
        x, y, isOpened = q.popleft()
        if board[x][y] == '1' :
            return visited[x][y][isOpened] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nIsOpened = isOpened
            if 0 <= nx < n and 0 <= ny < m :
                if 'a' <= board[nx][ny] <= 'f' :
                    nIsOpened = nIsOpened | (1<<(ord(board[nx][ny])-ord('a'))) 
                elif 'A' <= board[nx][ny] <= 'F' and (not nIsOpened & (1<<(ord(board[nx][ny])-ord('A')))) :
                    continue
                if not visited[nx][ny][nIsOpened] and board[nx][ny] != '#' :
                    visited[nx][ny][nIsOpened] = visited[x][y][isOpened] + 1
                    q.append((nx, ny, nIsOpened))
    return -1

n, m = map(int, sys.stdin.readline().strip().split())
board = [[0] * m for _ in range(n)]
visited = [[[0] * 2**6 for _ in range(m)] for __ in range(n)]
for i in range(n):
    board[i] = list(map(str, sys.stdin.readline().strip()))
    for j in range(m):
        if board[i][j] == '0' :
            start = (i, j, 0)
print(bfs(start))