# 풀이일자 : 2020/05/03
# 문제 이름 : 물통
# 문제 번호 : 2251
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 물통 C에 담겨있을 수 있는 용량
import sys
from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        z = c - x - y
        if not x:
            result.append(z)
        water = min(x, b-y)
        if not visited[x-water][y+water]:
            visited[x-water][y+water] = True
            q.append((x-water, y+water))
        water = min(x, c-z)
        if not visited[x-water][y]:
            visited[x-water][y] = True
            q.append((x-water, y))
        water = min(y, a-x)
        if not visited[x+water][y-water]:
            visited[x+water][y-water] = True
            q.append((x+water, y-water))
        water = min(y, c-z)
        if not visited[x][y-water]:
            visited[x][y-water] = True
            q.append((x, y-water))
        water = min(z, a-x)
        if not visited[x+water][y]:
            visited[x+water][y] = True
            q.append((x+water, y))
        water = min(z, b-y)
        if not visited[x][y+water]:
            visited[x][y+water] = True
            q.append((x, y+water))

result = []
a, b, c = map(int, sys.stdin.readline().strip().split())
visited = [[False]*(b+1) for _ in range(a+1)]
bfs()
for i in sorted(result) :
    print(i, end=" ")