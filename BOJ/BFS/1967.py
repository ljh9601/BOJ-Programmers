# 풀이일자 : 2020/04/23
# 문제 이름 : 트리의 지름
# 문제 번호 : 1967
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 입력으로 받은 트리의 지름
import sys
from collections import deque

def bfs(vertex):
    ans = 0
    standard = 0
    q = deque()
    visited = [False] * (nodeNum + 1)
    q.append(vertex)
    visited[vertex[0]] = True
    while q :
        current = q.pop()
        for i in path[current[0]] :
            if not visited[i[0]] :
                visited[i[0]] = True
                q.append((i[0], current[1] + i[1]))
                if current[1] + i[1] > ans :
                    ans = current[1] + i[1]
                    standard = i[0]
    return standard, ans

nodeNum = int(sys.stdin.readline().strip())
path = [[] for i in range(nodeNum+1)]
for i in range(nodeNum - 1):
    parent, child, weight = map(int, sys.stdin.readline().strip().split())
    path[parent].append([child, weight])
    path[child].append([parent, weight])
startPos = [bfs([1, 0])[0], 0]
print(bfs(startPos)[1])