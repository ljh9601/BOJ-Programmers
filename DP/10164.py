# 풀이일자 : 2020/04/03
# 문제 이름 : 격자상의 경로
# 문제 번호 : 19164
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 경로의 개수
# dp의 정의 : (n,m)번째 칸까지의 경로의 개수 (다만 k번호 칸까지의 dp값을 구하고 거기서 최종 점까지 경로를 다시 계산해야 함
import sys
import math

n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [[0] * (m+1) for i in range(n+1)]
dp = [[0] * (m+1) for i in range(n+1)]
dp[1][1] = 1
count = 0
circleX = n
circleY = m
for i in range(1, n+1):
    for j in range(1, m+1):
        count += 1
        if count == k :
            circleX = i
            circleY = j
            break
    if count == k :
        break
for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1 :
            continue
        if (i > circleX and j < circleY) or (i < circleX and j > circleY) :
            dp[i][j] = 0
        else :
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[n][m])