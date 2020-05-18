'''
풀이일자 : 2020/05/18
문제 이름 : 돌다리 건너기
문제 번호 : 2602
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 다이나믹 프로그래밍
DP의 정의 : dp[i][j][k] (k = 0 or 1) -> 현재 i번째까지 진행했고, 찾는 문자열의 j번째를 찾을 차례이며, 현재 어떤 다리에 있는지
'''
import sys

a = sys.stdin.readline().strip()
devil = sys.stdin.readline().strip()
angel = sys.stdin.readline().strip()
dp = [[0] * 2 for _ in range(len(devil))] # 0 : 악마다리, 1 : 천사다리
dp[0] = [1, 1]
length = len(a)
length_d = len(devil)
for i in range(0, length_d) :
    for j in range(length-1, -1, -1) :
        if devil[i] == a[j] :
            dp[j+1][0] += dp[j][1]
        if angel[i] == a[j] :
            dp[j+1][1] += dp[j][0]
print(sum(dp[length]))