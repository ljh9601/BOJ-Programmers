import sys
sys.setrecursionlimit(10000)

def dfs(graph, current, visited):
    visited[current] = True
    for i in graph[current]:
        if visited[i] is False :
            dfs(graph, i, visited)

if __name__ == "__main__":
    count = 0
    n, m = list(map(int, input().split()))
    result = []
    path = [[] for i in range(n+1)]
    visited = [False]*(n+1)

    for i in range (0, m):
        start, end = map(int, sys.stdin.readline().split())
        path[start].append(end)
        path[end].append(start)
    #print(path)
    for i in range(1, n+1):
        if visited[i] is False:
            dfs(path, i, visited)
            count += 1
    print(count)