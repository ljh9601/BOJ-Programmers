n = int(input())

inputs = [[0] * 3 for i in range(n)]
for i in range(0, n):
    inputs[i] = list(map(int, input().split()))

dp = [[0] * 3 for i in range(n+1)]
dp[1] = inputs[0]

for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1] + inputs[i-1][0], dp[i-1][2] + inputs[i-1][0])
    dp[i][1] = min(dp[i-1][0] + inputs[i-1][1], dp[i-1][2] + inputs[i-1][1])
    dp[i][2] = min(dp[i-1][0] + inputs[i-1][2], dp[i-1][1] + inputs[i-1][2])

print(min(dp[n]))