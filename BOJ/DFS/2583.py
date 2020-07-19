# 풀이일자 : 2020/04/06
# 문제 이름 : 영역 구하기
# 문제 번호 : 2583
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 분리된 영역들의 개수와 넓이
# dfs 함수를 돌 조건에 진입할 때마다 count 증가하여 영역 개수를 구해주고, dfs 내에서 queue가 돌아가는 횟수만큼이 영역의 넓이이므로 카운팅해준다.

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

def dfs(posX, posY):
    global cnt
    cnt += 1
    space = 0
    q = deque()
    q.appendleft((posX, posY))
    visited[posX][posY] = True
    while q :
        space += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if paper[nx][ny] != -1 and visited[nx][ny] == 0 :
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
    return space

m, n, k = map(int, sys.stdin.readline().strip().split())
paper = [[0] * (m) for i in range(n)]
visited = [[False] * (m) for i in range(n)]
area = []
for i in range(k):
    startX, startY, endX, endY = map(int, sys.stdin.readline().strip().split())
    for j in range(startX, endX):
        for k in range(startY, endY):
            paper[j][k] = -1
for i in range(n):
    for j in range(m):
        if paper[i][j] != -1 and visited[i][j] == 0:
            area.append(dfs(i, j))
print(cnt)
for i in sorted(area) :
    print(i, end=' ')