import sys

n = int(sys.stdin.readline().strip())
assert n <= 1000000
dp = [[0] * 10 for i in range(10)]
for i in range(10):
    dp[0][i] = 1
sumCnt = 9
resultIdx = (0, 0)
nth = 0
ans = ''
flag = False
if n <= 10 :
    print(n)
    exit()
for i in range(1, 10):
    if resultIdx != (0, 0):
        break
    for j in range(i, 10):
        dp[i][j] =dp[i][j-1] + dp[i-1][j-1]
        sumCnt += dp[i][j]
        if sumCnt >= n:
            flag = True
            resultIdx = (i, j)
            nth = dp[i][j] - (sumCnt - n)
            break
# 4로 시작하는 네자리수
# 4로 시작하는 세자리수
for i in range(10):
    print(dp[i])
print(resultIdx)
print(nth)
if not flag :
    print(-1)
    exit()
ans+= str(resultIdx[1]) # 4
howMany = resultIdx[0]+1 # 두자리수
while len(ans) < howMany :
    sumCnt = 0
    for i in range(resultIdx[1]):
        sumCnt += dp[resultIdx[0]-1][i]
        if sumCnt >= nth :
            resultIdx = (resultIdx[0]-1, i)
            nth = dp[resultIdx[0]][i] - (sumCnt - nth)
            ans += str(resultIdx[1])
            break
print(ans)