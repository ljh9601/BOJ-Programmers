n = int(input())

cards = []
cards = list(map(int,input().split()))
cards.insert(0, 0)

dp = []
dp.append(0)

maxSum = 0
for i in range (1, n+1):
    dp.append(-1)
    for j in range(1, i+1):
        dp[i] = max(dp[i],dp[i-j] + cards[j])

print(dp[n])