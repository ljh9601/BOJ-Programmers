'''
네트워크
'''


import sys
from collections import deque

def dfs(start, graph, visited):
    count = 0
    visited[start] = True
    stack = deque()
    stack.append(start)
    while stack :
        current = stack.pop()
        for item in graph[current]:
            if not visited[item] :
                visited[item] = True
                stack.append(item)

def solution(n, computers):
    cnt = 0
    visited = [False] * n
    graph = {}
    for i in range(n):
        graph[i] = set([])
        for j in range(n):
            if i == j :
                continue
            elif computers[i][j] == 1:
                graph[i].add(j)
    for i in range(n):
        if not visited[i] :
            dfs(i, graph, visited)
            cnt += 1
    return cnt