'''
풀이일자 : 2020/05/13
문제 이름 : 성곽
문제 번호 : 2234
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 다이나믹 프로그래밍
1. 이 성에 있는 방의 개수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
'''
import sys
from collections import deque
#11 : 2^3 + 2 + 1 = 1011

# 남, 동, 북, 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def wallInfo(detail) :
    canGo = []
    val = list(bin(detail))[2:]
    for i in range(len(val)) :
        val[i] = int(val[i])
    for i in range(4) :
        length = len(val)
        while length < 4 :
            val.insert(0, 0)
            length += 1
        if val[i] == 0 :
            canGo.append(i)
    return canGo

def bfs(posX, posY) :
    q = deque()
    q.appendleft((posX, posY))
    visited[posX][posY] = True
    width = 1
    while q :
        x, y = q.popleft()
        for i in board[x][y]:
            for j in i :
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < m and 0 <= ny < n :
                    if not visited[nx][ny] :
                        visited[nx][ny] = True
                        width += 1
                        q.append((nx, ny))
    return width

n, m = map(int, sys.stdin.readline().strip().split())
board = [[[] for _ in range(n)] for __ in range(m)]
visited = [[False] * n for _ in range(m)]
roomNo = 0
roomWidth = []
for i in range(m):
    info = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(n):
        board[i][j].append(wallInfo(info[j]))
for i in range(m):
    for j in range(n):
        if not visited[i][j] :
            roomNo += 1
            roomWidth.append(bfs(i, j))
print(roomNo)
print(max(roomWidth))