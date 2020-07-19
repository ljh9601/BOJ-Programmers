import sys

n = int(sys.stdin.readline().strip())
dp = []
dp.append(0)
dp.append(1)
dp.append(2)

for i in range(3, n+1):
    temp = (dp[i-1] % 15746) + (dp[i-2] % 15746)
    dp.append(temp % 15746)
print(dp[n] % 15746)