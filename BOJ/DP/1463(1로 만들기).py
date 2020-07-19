# x=0 -> 0
# x=1 -> 0
# x=2 -> 1
# x=3 -> 1

# x=4 -> 2

# dp[x] = dp[x-1] + 1
# dp[x] = dp[x/2] + 1
# dp[x] = dp[x/3] + 1

n = int(input())

dp = []

dp.append(0) # x=0
dp.append(0) # x=1
dp.append(1) # x=2
dp.append(1) # x=3

for i in range(4, n + 1):
    dp.append(dp[i - 1] + 1)
    if(i % 2 == 0):
        dp[i] = min(dp[i], dp[int(i / 2)] + 1)
    if(i % 3 == 0):
        dp[i] = min(dp[i], dp[int(i / 3)] + 1)

print(dp[n])