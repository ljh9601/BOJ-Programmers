import sys
input = sys.stdin.readline().strip()
n, k = map(int, input.split())
dp = [[0] * (k+1) for i in range(n+1)]
dp[1][1] = 1

for i in range(1, k+1):
    dp[1][i] = i
for i in range(1, n+1):
    dp[i][1] = 1

for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[n][k] % 1000000000)