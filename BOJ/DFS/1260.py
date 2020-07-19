def bfs(graph, start):
    visited = []
    queue = []
    queue.append(start)
    while queue :
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
        for i in sorted(graph[current], reverse=False):
            if i not in visited :
                queue.append(i)

    return visited

def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)
    while stack :
        current = stack.pop()
        if current not in visited:
            visited.append(current)
        for i in sorted(graph[current], reverse=True):
            if i not in visited :
                stack.append(i)

    return visited

if __name__ == "__main__":
    n, m, v = list(map(int, input().split()))
    path = {}

    for i in range (0, m):
        start, end = list(map(int, input().split()))
        if start not in path:
            path[start] = set([])
        if end not in path:
            path[end] = set([])
        path[start].add(end)
        path[end].add(start)
    if v not in path:
        print(v)
        print(v)
    else:
        print(" ".join(map(str, dfs(path, v))))
        print(" ".join(map(str, bfs(path, v))))

