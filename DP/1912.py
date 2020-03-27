n = int(input())

inputs = []
inputs = list(map(int, input().split()))

dp = []
dp.append(-1001)

for i in range(0, n):
    dp.append(max(dp[i] + inputs[i], inputs[i]))

print(max(dp))