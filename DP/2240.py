# 풀이일자 : 2020/04/18
# 문제 이름 : 자두나무
# 문제 번호 : 2240
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 자두가 받을 수 있는 자두의 개수
# dp의 정의 :
import sys

t, w = map(int, sys.stdin.readline().strip().split())
# dp[1][2][1] : 2초가 되기 직전 현재 나무와 다른 나무로 이동했을 때 자두는 현재 1번 나무에 있고, 이 상황까지의 최댓값
dp = [[[0] * (w+2) for _ in range(t+1)] for __ in range(3)] 
drop = [int(sys.stdin.readline().strip()) for _ in range(t)]

for i in range(1, t+1) :
    for j in range(1, w+2) :
        if drop[i-1] == 1 :
            dp[1][i][j] = max(dp[1][i-1][j], dp[2][i-1][j-1]) + 1
            dp[2][i][j] = max(dp[1][i-1][j-1], dp[2][i-1][j])
        else :
            if i == 1 and j == 1 :
                continue
            dp[1][i][j] = max(dp[2][i-1][j-1], dp[1][i-1][j])
            dp[2][i][j] = max(dp[1][i-1][j-1], dp[2][i-1][j]) + 1

print(max(max(dp[1][t]), max(dp[2][t])))