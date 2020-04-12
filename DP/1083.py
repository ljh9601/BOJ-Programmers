# 풀이일자 : 2020/04/12
# 문제 이름 : 감소하는 수
# 문제 번호 : 1083
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# n번째로 감수하는 수
# DP의 정의 : 2차원 배열로 (i,j)는 j로 시작하는 (i+1)자릿수이다.
# ex) (2, 4) -> 4로 시작하는 세자리수
# dp[2][4]는 1~3으로 시작하는 두자릿수에 앞에다가 4를 붙인 것이므로, dp[1]부터 dp[0]까지 거슬러 올라가며 dp[x][y]를 구해주고, 결과값에 y를 append해주면 됨.

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
if not flag :
    print(-1)
    exit()
ans+= str(resultIdx[1])
howMany = resultIdx[0]+1
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