import sys

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    if x == n-1 and y == n-1:
        return 1
    if dp[x][y] != -1 :
        return dp[x][y]
    dp[x][y] = 0
    for i in range(0, 2):
        nx = x + inputs[x][y] * dx[i]
        ny = y + inputs[x][y] * dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            dp[x][y] += dfs(nx, ny)         
    return dp[x][y]

n = int(sys.stdin.readline().strip())
inputs = [[0] * n for i in range(n)]
dp = [[-1] * n for i in range(n)]
for i in range(n):
    inputs[i] = list(map(int, sys.stdin.readline().strip().split()))

print(dfs(0, 0))