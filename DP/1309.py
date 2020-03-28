import sys

input = sys.stdin.readline().strip()
n = int(input)
assert 1 <= n <= 100000

dp = [1] * (n+1)
dp[1] = 3
for i in range(2, n+1):
    dp[i] = ((2 * dp[i-1]) % 9901 + dp[i-2] % 9901) % 9901
print(dp[n] % 9901)