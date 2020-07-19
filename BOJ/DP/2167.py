import sys

n, m = map(int, sys.stdin.readline().strip().split())
dp = [[0] * (m+1) for i in range(n+1)]
arr = [[0] * m for i in range(n)]
result = []
for i in range (n):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

v = int(sys.stdin.readline().strip())
for i in range(v):
    x, y, z, w = map(int, sys.stdin.readline().strip().split())
    result.append(dp[z][w] - dp[z][y - 1] - dp[x - 1][w] + dp[x - 1][y - 1])
print("\n".join(map(str, result)))