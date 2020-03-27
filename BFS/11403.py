from collections import deque

def bfs(graph, adj, start, end):
    visited = []
    queue = deque()
    queue.append(start)

    while queue :
        current = queue.popleft()
        if end in graph[current] :
            adj[start][end] = 1
            break
        if current not in visited :
            visited.append(current)
        for i in graph[current]:
            if i not in visited :
                queue.append(i)

if __name__ == "__main__":
    n = int(input())
    graph = {}
    adj = [[0] * n for i in range(n)]
    for i in range(n):
        inputs = list(map(int, input().split()))
        if i not in graph :
            graph[i] = set([])
        for j in range(n):
            if inputs[j] is 1 :
                graph[i].add(j)
    for i in range(n):
        for j in range(n):
            bfs(graph,adj, i, j)
    for i in adj :
        for j in i :
            print(j, end = ' ')
        print()
