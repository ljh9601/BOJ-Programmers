# 풀이일자 : 2020/04/08
# 문제 이름 : 나이트의 이동
# 문제 번호 : 7562
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 나이트의 이동 횟수
# 기본적인 BFS에 direction만 정의해주면 되는 문제.

import sys
from collections import deque
directrion = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
ans = []

def bfs(start, end):
    startX, startY = start[0], start[1]
    endX, endY = end[0], end[1]
    visited[startX][startY] = 1
    q = deque()
    q.appendleft((startX, startY))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + directrion[i][0]
            ny = y + directrion[i][1]
            if 0 <= nx < width and 0 <= ny < width :
                if nx == endX and ny == endY :
                    visited[nx][ny] = visited[x][y] + 1
                    return visited[nx][ny]-1
                elif not visited[nx][ny] :
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return visited[endX][endY]-1


tcNum = int(sys.stdin.readline().strip())
for i in range(tcNum):
    width = int(sys.stdin.readline().strip())
    visited = [[0] * width for i in range(width)]
    start = list(map(int, sys.stdin.readline().strip().split()))
    end = list(map(int, sys.stdin.readline().strip().split()))
    if start[0] == end[0] and start[1] == end[1] :
        ans.append(0)
    else:
        ans.append(bfs(start, end))
for i in ans :
    print(i)