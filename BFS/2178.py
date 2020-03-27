def bfs(maze, n, m):
    visited = [[0] * m for i in range(n)]
    
    visited[0][0] = 1
    queue = []
    queue.append((0, 0))

    # 아래, 위, 왼쪽, 오른쪽
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.pop(0)
        if x == n-1 and y == m-1 :
            print(visited[x][y])
            break
        for i in range (0, 4):
            ax = x + dx[i]
            ay = y + dy[i]
            if ax >= 0 and ax < n and ay >= 0 and ay < m:
                if visited[ax][ay] == 0 and maze[ax][ay] == 1:
                    visited[ax][ay] = visited[x][y] + 1
                    queue.append((ax, ay))

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    maze = [[0] * m for i in range (n)]
    
    start = (0, 0)
    end = (n, m)

    for i in range(0, n):
        inputs = str(input())
        for j in range (0, m):
            maze[i][j] = int(inputs[j])
    bfs(maze, n, m)

