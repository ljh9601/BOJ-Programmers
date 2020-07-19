# 풀이일자 : 2020/04/07
# 문제 이름 : 토마토
# 문제 번호 : 7569
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 토마토가 모두 익을 때까지 걸리는 일수
# 3차원 배열을 활용하여 direction을 재정의하고 각 방향으로 BFS 돌리면 됨.
import sys
from collections import deque

direction = [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]
ans = 0

def bfs(q, cnt):
    global ans

    while q :
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            nz = z + direction[i][2]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if warehouse[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                    cnt -= 1
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append((nx, ny, nz))
                    if visited[nx][ny][nz] - 1 > ans :
                        ans = visited[nx][ny][nz] - 1
    return cnt
                

m, n, h = map(int, sys.stdin.readline().strip().split())
warehouse = [[[0] * m for i in range(n)] for i in range(h)]
visited = [[[0] * m for i in range(n)] for i in range(h)]
cntYet = 0
cntAlready = 0
for i in range(h):
    for j in range(n):
        warehouse[i][j] = list(map(int, sys.stdin.readline().strip().split()))

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if warehouse[i][j][k] == -1 :
                visited[i][j][k] = -1
            if warehouse[i][j][k] == 0 :
                cntYet += 1
            if warehouse[i][j][k] == 1:
                visited[i][j][k] = 1
                cntAlready += 1
                queue.append((i, j, k))
if cntYet == 0 and cntAlready > 0:
    print(0)
    exit()
elif cntYet == 0 and cntAlready == 0 :
    print(-1)
    exit()
        

#모든 토마토가 익지 못하는 상황
if bfs(queue, cntYet) > 0 :
    print(-1)
    exit()
print(ans)