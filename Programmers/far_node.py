'''
가장 먼 노드
풀이일자 : 2020.06.10
'''

from collections import deque

def bfs(graph, n):
    q = deque()
    visited = [0] * (n+1)
    q.appendleft(1)
    visited[1] = 1
    while q :
        current = q.popleft()
        for item in graph[current] :
            if not visited[item] :
                visited[item] = visited[current] + 1
                q.append(item)
    return visited

def solution(n, edge):
    path = dict()
    for i in range(len(edge)):
        s, e = edge[i]
        if s not in path :
            path[s] = set([])
        if e not in path :
            path[e] = set([])
        path[s].add(e)
        path[e].add(s)
    result = bfs(path, n)
    maxVal = max(result)
    ans = 0
    for value in result :
        if maxVal == value :
            ans += 1 
    return ans