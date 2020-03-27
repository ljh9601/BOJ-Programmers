#1 : 1 #2 : 2 #3 : 3 #4 : 4 #5 : 1 #6 : 2 #7 : 3 #8 : 4 #9 : 5 #10 : 2 #11 : 3

inputs = list(map(int,input().split()))
count = inputs[0] #3
value = inputs[1] #15

coins = []
for i in range (0, count):
    coins.append(int(input())) # 1, 5, 12

dp = []
dp.append(0)

for i in range(1, value + 1):
    temp = 100001
    for j in range(0, count):
        if i - coins[j] >= 0:
            temp= min(temp, dp[i - coins[j]] + 1)
    dp.append(temp)

if dp[value] == 100001:
    print(-1)
else:
    print(dp[value])