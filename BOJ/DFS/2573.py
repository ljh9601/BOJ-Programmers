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

years = 0
n, m = map(int, sys.stdin.readline().strip().split())
board = [[0] * m for i in range(n)]
notMelted = []

def dfs(notMelted):
    global years
    global board
    while True :
        if len(notMelted) == 0 :
            print(0)
            exit()
        count = 0
        visited = [[0] * m for i in range(n)]
        stack = deque()
        stack.append(notMelted[0])
        while stack :
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if board[nx][ny] > 0 and not visited[nx][ny] :
                    count += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        if years == 0 :
            if len(notMelted) != count :
                return years
        length = len(notMelted)
        notMelted = makeNewBoard()
        if length == 1 :
            return 0
        if length != count :
            return years
        years += 1
    return 0

def makeNewBoard():
    global notMelted
    global board
    countBoard = [[0] * m for i in range(n)]
    notMelted = []
    for i in range(0, n):
        for j in range(0, m):
            if board[i][j] > 0 :
                count = 0
                for k in range(4):
                    if 0 <= i + dx[k] < n and 0 <= j + dy[k] < m :
                        if board[i + dx[k]][j + dy[k]] == 0 :
                            count += 1
                countBoard[i][j] = count
    for i in range(n):
        for j in range(m):
            board[i][j] = board[i][j] - countBoard[i][j]
            if board[i][j] < 0 :
                board[i][j] = 0
            if board[i][j] > 0 :
                notMelted.append((i, j))
    return notMelted


for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(m):
        if board[i][j] > 0 :
            notMelted.append((i, j))
print(dfs(notMelted))