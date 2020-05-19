'''
풀이일자 : 2020/05/19
문제 이름 : 열쇠
문제 번호 : 9328
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : BFS
상근이가 훔칠 수 있는 문서의 최대 개수
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(startX, startY):
    q = deque()
    q.append((startX, startY))
    visited = [[False] * (w+2) for _ in range(h+2)]
    visited[startX][startY] = True
    cnt = 0
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h+2 and 0 <= ny < w+2 :
                if not visited[nx][ny] :
                    if board[nx][ny] == '$' :
                        cnt += 1
                        board[nx][ny] = '.'
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    elif board[nx][ny] == '.' :
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    elif 'a' <= board[nx][ny] <= 'z' :
                        q = deque()
                        visited = [[False] * (w+2) for _ in range(h+2)]
                        q.append((nx, ny))
                        keys.append(board[nx][ny])
                        board[nx][ny] = '.'
                    elif board[nx][ny].isupper() :
                        if board[nx][ny].lower() in keys :
                            board[nx][ny] = '.'
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt

tcNum = int(sys.stdin.readline().strip())
for _ in range(tcNum) :
    h, w = map(int, sys.stdin.readline().strip().split())
    board = [list(map(str, sys.stdin.readline().strip())) for __ in range(h)]
    keys = list(map(str, sys.stdin.readline().strip()))
    for i in range(h):
        for j in range(w):
            if board[i][j].isupper():
                if board[i][j] in keys:
                    board[i][j] = '.'
    for i in board:
        i.insert(0, '.')
        i.append('.')
    board.insert(0, ['.']*(w+2))
    board.append(['.']*(w+2))

    print(bfs(0, 0))