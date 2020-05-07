# 풀이일자 : 2020/05/07
# 문제 이름 : 계단수
# 문제 번호 : 1562
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 길이가 N이면서 0~9가 모두 등장하는 계단수의 개수
# DP의 정의 : dp[i][j] : i자릿수
# dp[n][x][a] = n이라는 길이의 계단수 맨 마지막 숫자가 x로 끝날때 a라는 비트 정보를 가지고 있는 방법의 수
# 0~9까지의 숫자 사용 여부를 확인할 수 있도록 비트 10자리 (2^10)을 사용한다. -> bitmask
import sys
n = int(sys.stdin.readline().strip())

dp = [[0] * 1024 for _ in range(10)]
 
for i in range(1, 10):
    dp[i][1<<i] = 1

for i in range(1, n):
    new_dp = [[0 for _ in range(1024)] for _ in range(10)]
    for e in range(10):
        for bm in range(1024):
            if e < 9:
                new_dp[e][bm | (1<<e)] = (new_dp[e][bm | (1<<e)] + dp[e+1][bm]) % 1000000000
            if e > 0:
                new_dp[e][bm | (1<<e)] = (new_dp[e][bm | (1<<e)] + dp[e-1][bm]) % 1000000000
    dp = new_dp

print(sum([dp[i][1023] for i in range(10)]) % 1000000000)