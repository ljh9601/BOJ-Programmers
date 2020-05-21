'''
풀이일자 : 2020/05/21
문제 이름 : 동전 바꿔주기
문제 번호 : 2624
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 다이나믹 프로그래밍
동전 교환 방법의 가짓수
'''
import sys

t = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
coins = []
dp = [[0] * (t+1) for _ in range(k+1)]
for i in range(0, k) :
    p, n = map(int, sys.stdin.readline().strip().split())
    coins.append([p, n])
coins.sort()
dp[0][0] = 1
for i in range(1,k+1):
    for j in range(coins[i-1][1]+1):
        for m in range(t+1):
            if m >= coins[i-1][0]*j:
                dp[i][m] += dp[i-1][m - coins[i-1][0]*j]
print(dp[k][t])