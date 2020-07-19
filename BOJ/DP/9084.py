# 풀이일자 : 2020/04/10
# 문제 이름 : 동전
# 문제 번호 : 1707
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DP
# 금액을 세는 모든 방법의 수
# DP의 정의 : n원을 세는 경우의 수
import sys
tcNum = int(sys.stdin.readline().strip())
for i in range(tcNum):
    coinNum = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().strip().split()))
    goal = int(sys.stdin.readline().strip())
    dp = [0] * (goal+1)
    dp[0] = 1
    for i in coins :
        for j in range(1, goal+1):
            if j >= i:
                dp[j] += dp[j-i]
    print(dp[goal])