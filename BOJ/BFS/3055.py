# 풀이일자 : 2020/04/15
# 문제 이름 : 탈출
# 문제 번호 : 3055.py
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start, end, water):
    qS = deque()
    tempQS = deque()
    qW = deque()
    qS.appendleft(start)
    length = len(water)
    for i in water :
        qW.append(i)
    while qS :
        for _ in range(length) :
            xW, yW = qW.popleft()
            for i in range(4):
                nxW = xW + dx[i]
                nyW = yW + dy[i]
                if 0 <= nxW < r and 0 <= nyW < c :
                    if visited[nxW][nyW] == 0 and board[nxW][nyW] == '.':
                        visited[nxW][nyW] = -1
                        qW.append((nxW, nyW))
        length = len(qW)    
        tempQS = qS
        qS = deque()
        while tempQS :
            xS, yS = tempQS.popleft()
            for i in range(4):
                nxS = xS + dx[i]
                nyS = yS + dy[i]
                if 0 <= nxS < r and 0 <= nyS < c :
                    if nxS == end[0] and nyS == end[1] :
                        visited[nxS][nyS] = visited[xS][yS] + 1
                        return visited[nxS][nyS]
                    if visited[nxS][nyS] == 0 and (board[nxS][nyS] == '.' or board[nxS][nyS] == 'D'):
                        visited[nxS][nyS] = visited[xS][yS] + 1
                        qS.append((nxS, nyS))    
    return 0

r, c = map(int, sys.stdin.readline().strip().split())
board = [['0'] * c for i in range(r)]
visited = [[0] * c for i in range(r)]
water = []
for i in range(r):
    board[i] = sys.stdin.readline().strip()
    for j in range(c):
        if board[i][j] == 'S' :
            start = (i, j)
        if board[i][j] == 'D' :
            end = (i, j)
        if board[i][j] == '*' :
            water.append((i, j))
ans = bfs(start, end, water)
print(ans if ans > 0 else 'KAKTUS')