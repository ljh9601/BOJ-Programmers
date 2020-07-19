def bfs(arr, start, n, visited, result):
    queue = []
    queue.append(start)
    count = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y = queue.pop(0)
        for i in range(0, 4):
            ax = x + dx[i]
            ay = y + dy[i]
            if ax >= 0 and ax < n and ay >= 0 and ay < n:
                if visited[ax][ay] == 0 and int(arr[ax][ay]) == 1:
                    count += 1
                    visited[ax][ay] = 1
                    queue.append((ax, ay))
    if count is 0 : 
        result.append(1)
    else:
        result.append(count)

if __name__ == "__main__":

    n = int(input())
    start = (0, 0)
    arr = []
    apart = []
    result = []
    visited = [[0] * n for i in range (n)]

    for i in range (0, n):
        arr.append(str(input()))
        for j in range(0, n):
            if int(arr[i][j]) is 1:
                apart.append((i, j))

    for i in range(0, n):
        for j in range(0, n):
            if int(arr[i][j]) is 1 and visited[i][j] is 0:
                start = (i, j)
                bfs(arr, start, n, visited, result)
    
    print(len(result))
    if len(result)>0:
        for i in sorted(result):
            print(i)
    
    
