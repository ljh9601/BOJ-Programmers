import sys

n = int(sys.stdin.readline().strip())
inputs = []
leftDp = []
rightDp = [0 for i in range(n)]
result = []
inputs = list(map(int, sys.stdin.readline().strip().split()))
leftDp.append(1)

for i in range(1, n):
    bigger = []
    standard = inputs[i]
    for j in range(0, i):
        if standard > inputs[j]: 
            bigger.append(leftDp[j])
    if not bigger:
        leftDp.append(1)
    else:
        tempVal = max(bigger) + 1
        leftDp.append(tempVal)
for i in range(n-1, -1, -1):
    smaller = []
    standard = inputs[i]
    for j in range(n-1, i, -1):
        if standard > inputs[j]:
            smaller.append(rightDp[j])
    if not smaller:
        rightDp[i] = 1
    else:
        tempVal = max(smaller) + 1
        rightDp[i] = tempVal
for i in range(n):
    result.append(leftDp[i] + rightDp[i] - 1)
print(max(result))