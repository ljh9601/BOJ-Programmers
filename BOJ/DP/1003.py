import sys

n = int(sys.stdin.readline().strip())
inputs = []
for i in range(0, n):
    inputs.append(int(sys.stdin.readline().strip()))

dp = [[0]*2 for i in range(100)]

dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, max(inputs)+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in inputs:
    print('{0} {1}'.format(dp[i][0], dp[i][1]))