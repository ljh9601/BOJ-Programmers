n = int(input())
score = []
dp = []

for i in range (0, n):
    score.append(int(input()))
if n == 1:
    print(score[0])
elif n == 2 :
    print(score[0] + score[1])
else :
    dp.append(score[0])
    dp.append(score[0] + score[1])
    dp.append(max(score[1] + score[2], score[0] + score[2]))

    for i in range(3, n):
        dp.append(max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i]))
    print(dp[n-1])