# 풀이일자 : 2020/08/27
# 문제 이름 : 알고스팟
# 문제 번호 : 1261
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지

import heapq
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    q = []
    heapq.heappush(q, (0, 0, 0))
    visited = [[False] * m for _ in range(n)]
    while q :
        cnt, x, y = heapq.heappop(q)
        if x == n-1 and y == m-1 :
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] :
                    visited[nx][ny] = True
                    if arr[nx][ny] == 1 :
                        heapq.heappush(q, (cnt + 1, nx, ny))
                    else :
                        heapq.heappush(q, (cnt, nx, ny))
    return cnt

m, n = list(map(int, sys.stdin.readline().strip().split()))
arr = [list(sys.stdin.readline()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        arr[i][j] = int(arr[i][j])
print(bfs([0, 0, 0]))