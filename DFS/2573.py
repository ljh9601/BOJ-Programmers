# 풀이일자 : 2020/04/14
# 문제 이름 : 빙산
# 문제 번호 : 2573.py
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 빙산이 두 덩어리 이상 분리되는 최초의 시간
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(posX, posY):
    stack = deque()
    stack.append((posX, posY))
    while stack :
        count = 0
        newBoard = [[0] * m for i in range(n)]
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if board[nx][ny] > 0 and not visited[nx][ny] :
                
                visited[nx][ny] = True
                stack.append((nx, ny))
        board = newBoard

def makeNewBoard(i, j):
    count = 0
    if board[i][j] > 0 :
        for k in range(4):
            if not board[i + dx[k]][j + dy[k]] :
                count += 1
    return count

n, m = map(int, sys.stdin.readline().strip().split())
board = [[0] * m for i in range(n)]
visited = [[0] * m for i in range(n)]
notMelted = []
howManyMelt = []
for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(m):
        if board[i][j] > 0 :
            notMelted.append((i, j))

