n = int(input())

dp = []
dp.append(0)
dp.append(1)
dp.append(3)
 
for i in range(3,n+1):
    dp.append(dp[i-1] + (2 * dp[i-2]))

print(dp[n] % 10007)