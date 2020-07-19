import sys

m, n = list(map(int, sys.stdin.readline().strip().split()))
arr = [[0] * n for i in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dp = [[-1] * n for i in range(m)]

def dfs(x, y):
    if x == m-1 and y == n-1 :
        return 1
    if dp[x][y] != -1 :
        return dp[x][y]
    dp[x][y] = 0
    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if arr[nx][ny] < arr[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


for i in range(m):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))

print(dfs(0, 0))