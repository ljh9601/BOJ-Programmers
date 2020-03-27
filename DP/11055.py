import sys

n = int(sys.stdin.readline().strip())
inputs = list(map(int, sys.stdin.readline().strip().split()))
dp = []
temp = []
dp.append(inputs[0])
for i in range(1, n):
    temp = []
    for j in range(0, i):
        if inputs[i] > inputs[j] :
            temp.append(dp[j])
    if not temp :
        dp.append(inputs[i])
    else :
        dp.append(max(temp) + inputs[i])
print(max(dp))