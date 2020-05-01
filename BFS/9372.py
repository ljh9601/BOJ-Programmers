# 풀이일자 : 2020/05/01
# 문제 이름 : 상근이의 여행
# 문제 번호 : 9372
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
import sys
from collections import deque

def bfs(start):
    q = deque()
    q.appendleft(start)
    visited[start] = 1
    count = 0
    while q :
        count += 1
        current = q.popleft()
        for item in path[current] :
            if not visited[item] :
                q.append(item)
                visited[item] = visited[current] + 1
    return count - 1

tcNum = int(sys.stdin.readline().strip())
for _ in range(tcNum) :
    n, m = map(int, sys.stdin.readline().strip().split())
    path = {}
    visited = [0] * (n+1)
    for i in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        if a not in path :
            path[a] = set([])
        if b not in path :
            path[b] = set([])
        path[a].add(b)
        path[b].add(a)
    print(bfs(a))