n = int(input())

inputs = []
for i in range(0, n):
    inputs.append(list(map(int, input().split())))

dp = []
for i in range (0, n+1):
    dp.append([0] * i)

dp[0] = 0
dp[1] = inputs[0]

for i in range (2, n+1):
    dp[i][0] = dp[i-1][0] + inputs[i-1][0]
    for j in range (1, i-1):
        dp[i][j] = max(dp[i-1][j-1] + inputs[i-1][j], dp[i-1][j] + inputs[i-1][j])
    dp[i][i-1] = dp[i-1][i-2] + inputs[i-1][i-1]

print(max(dp[n]))