import sys
import math

n = int(sys.stdin.readline().strip())
dp = []
dp.append(0)
for i in range(1, n+1) :
    j = 1
    dp.append(1000000)
    while j * j <= i :
        if dp[i] > dp[i - j * j] + 1 :
            dp[i] = dp[i - j * j] + 1
        j += 1
print(dp[n])