import sys

n = int(sys.stdin.readline().strip())
inputs = list(map(int, sys.stdin.readline().strip().split()))
dp = []
dp.append(1)
for i in range(1, len(inputs)):
    temp = []
    for j in range(0, i):
        if inputs[j] > inputs[i]:
            temp.append(dp[j])
    if not temp:
        dp.append(1)
    else:
        tempVal = max(temp) + 1
        dp.append(tempVal)
print(max(dp))