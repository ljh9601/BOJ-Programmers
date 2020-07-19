import sys

n = int(input())

result = []
time = []
payment = []

dp = []

for i in range(n):
    t, p = map(int, sys.stdin.readline().strip().split())
    time.append(t)
    payment.append(p)
    dp.append(p)

dp.append(0)
for i in range(n-1, -1, -1):
    if time[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i + 1], payment[i] + dp[i + time[i]])
print(dp[0])
