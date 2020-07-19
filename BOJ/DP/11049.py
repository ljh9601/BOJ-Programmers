# 풀이일자 : 2020/04/01
# 문제 이름 : 행렬 곱셈 순서
# 문제 번호 : 11049
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 곱셈 연산의 최솟값
# dp의 정의 : i,j 부터 n,m(n,m > i,j) 까지의 행렬곱의 최솟값
import sys

n = int(sys.stdin.readline().strip())
inputs = [[0] * 2 for i in range(n)]
for i in range(n):
    inputs[i] = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * n for i in range(n)]
for i in range(1, n):
    for j in range(0, n-i):
        if i == 1:
            dp[j][j+i] = inputs[j][0] * inputs[j][1] * inputs[j+i][1]
            continue
        dp[j][j+i] = 2**32
        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + inputs[j][0] * inputs[k][1] * inputs[j+i][1])
                
print(dp[0][n-1])