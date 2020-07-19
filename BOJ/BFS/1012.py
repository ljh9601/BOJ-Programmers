from collections import deque

def bfs(arr, start, result, visited):
    count = 0
    queue = deque()
    queue.append(start)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range (0, 4):
            ax = x + dx[i]
            ay = y + dy[i]
            if ax >= 0 and ax < n and ay >= 0 and ay < m:
                if visited[ax][ay] == 0 and arr[ax][ay] == 1:
                    visited[ax][ay] = 1
                    count += 1
                    queue.append((ax, ay))
    result.append(count)
        
if __name__ == "__main__":
    cases = int(input())
    output = []

    for i in range(0, cases):
        result = []
        n, m, v = list(map(int, input().split()))
        arr = [[0] * m for j in range (n)]
        visited = [[0] * m for j in range (n)]
        for k in range(0, v):
            x, y = list(map(int, input().split()))
            arr[x][y] = 1
        
        for i in range(0, n):
            for j in range(0, m):
                if arr[i][j] is 1 and visited[i][j] is 0:
                    start = (i, j)
                    bfs(arr, start, result, visited)
        output.append(len(result))
    
    for i in output:
        print(i)