# 풀이일자 : 2020/04/09
# 문제 이름 : 이분 그래프
# 문제 번호 : 1707
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 이분그래프인지 아닌지 판별.
import sys
from collections import deque

def bfs(pos, visited, color):
    q = deque([pos])
    color[pos] = 1
    visited[pos] = True
    while q and flag :
        current = q.popleft()
        for idx in path[current]:
            if not visited[idx]:
                q.append(idx)
                color[idx] = 3 - color[current]
                visited[idx] = True
            else :
                if color[current] == color[idx]:
                    return False
    return True
tcNum = int(sys.stdin.readline().strip())
for i in range(tcNum):
    v, e = map(int, sys.stdin.readline().strip().split())
    path = [[] for i in range(v+1)]
    visited = [False for _ in range(v + 1)]
    color = [0 for _ in range(v + 1)]
    flag = True
    for j in range(e):
        start, end = map(int, sys.stdin.readline().strip().split())
        path[start].append(end)
        path[end].append(start)
    for k in range(1, v+1):
        if not visited[k] :
            if not bfs(k, visited, color):
                flag = False
                break
    print('YES' if flag else 'NO')