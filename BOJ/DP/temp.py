import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(posX, posY):
    for i in range(m):
        print(check[i])
    print()
    if posX == m-1 and posY == n-1 :
        return 1
    if check[posX][posY] != INF :
        return check[posX][posY]
    check[posX][posY] = 0

    for i in range(4):
        nx = posX + dx[i]
        ny = posY + dy[i]
        if 0 <= nx < m and 0 <= ny < n :
            if board[posX][posY] > board[nx][ny]:
                check[posX][posY] += dfs(nx, ny)

    return check[posX][posY]

m, n = map(int, sys.stdin.readline().strip().split()) # m : 세로, n : 가로
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
INF = 987654321
check = [[INF] * n for _ in range(m)]
print(dfs(0, 0))