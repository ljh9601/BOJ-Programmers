# 풀이일자 : 2020/04/13
# 문제 이름 : 촌수 계산
# 문제 번호 : 2644.py
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 두 사람의 촌수 계산
#기본적인 BFS 탐색 문제.
import sys
from collections import deque

def bfs(start, end):
    q = deque()
    q.appendleft(start)
    while q :
        current = q.popleft()
        if end in path[current] :
            visited[end] = visited[current]
            return visited[end]
        if not visited[current]:
            visited[current] = visited[current] + 1
        for i in path[current] :
            if not visited[i] :
                visited[i] = visited[current] + 1
                q.append(i)
    return -1

n = int(sys.stdin.readline().strip())
a, b = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())
visited = [0] * (n+1)
path = {}
for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    if x not in path :
        path[x] = set({})
    if y not in path :
        path[y] = set({})
    path[x].add(y)
    path[y].add(x)
print(bfs(a, b))