# 풀이일자 : 2020/03/30
# 작성자 : 이장행
# 문제 이름 : 가장 큰 정사각형
# 문제 번호 : 1915
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍 
# 가장 큰 정사각형의 크기
# dp의 정의 : (i, i)까지 만들 수 있는 가장 큰 정사각형의 크기
# 예제에서 dp[1][1] = 1, dp[2][2] = 4

import sys

n, m = map(int, sys.stdin.readline().strip().split())
assert 1 <= n, m <= 1000
arr = [['0'] * (m) for i in range(n)]
for i in range(n):
    tempStr = list(map(str, sys.stdin.readline().strip()))
    for j in range(0, m):
        arr[i][j] = tempStr[j]
dp = [[0] * (m+1) for i in range(n+1)]
maxVal = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if int(arr[i-1][j-1]) == 1 :
            dp[i][j] = min(dp[i-1][j],  dp[i-1][j-1],  dp[i][j-1]) + 1
            maxVal = dp[i][j] if dp[i][j] > maxVal else maxVal
for i in range(n+1):
    print(dp[i])
print(maxVal * maxVal)