'''
풀이일자 : 2020/05/17
문제 이름 : 줄어들지 않아
문제 번호 : 2688
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 다이나믹 프로그래밍
DP의 정의 : dp[i][j] : j로 끝나는 i자리수
'''

import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    dp = [[0] * 10 for __ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = 1
        for j in range(1, 10):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(sum(dp[n]))