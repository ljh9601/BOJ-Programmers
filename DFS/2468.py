# 풀이일자 : 2020/04/05
# 문제 이름 : 안전 영역
# 문제 번호 : 2468
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 안전한 영역의 최대 개수
# DFS를 이용하여 DFS를 돌 때마다 값을 1 증가시켜 visited에 저장하며 영역 개수 구함.

import sys
from collections import deque
from copy import deepcopy

ans = 10001

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(posX, posY, depth):
    global ans
    q = deque()
    q.appendleft((posX, posY))
    ans += 1
    visited[posX][posY] = ans
    while q :
        x, y = q.popleft()
        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]
            if nx >= 0 and nx < n and ny >= 0 and ny < n :
                if arr[nx][ny] > depth and not visited[nx][ny]:
                    visited[nx][ny] = ans
                    q.appendleft((nx, ny))

n = int(sys.stdin.readline().strip())
arr = [[0] * n for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))
maxDepth = -1
for i in range(n):
    for j in range(n):
        if arr[i][j] > maxDepth :
            maxDepth = arr[i][j]
result = [0] * (maxDepth + 1)
for i in range(maxDepth, -1, -1):
    visited = [[0] * n for i in range(n)]
    ans = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and visited[j][k] == False:
                dfs(j, k, i)
    result[i] = ans
print(max(result))