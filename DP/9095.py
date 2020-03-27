n = int(input())

inputs = []
for i in range (0, n):
    inputs.append(int(input()))

dp = []
dp.append(0)
dp.append(1)
dp.append(2)
dp.append(4)

for i in range(4, 11):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in range(0, n):
    print(dp[inputs[i]])