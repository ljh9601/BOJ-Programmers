# 풀이일자 : 2020/04/15
# 문제 이름 : 로봇 조종하기
# 문제 번호 : 2169
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 탐사한 지역들의 최대 가치
# DP의 정의 : (n,m) 까지 도달했을 때 탐사 가치의 최댓값을 저장.
# 세로 index가 홀수일 때는 오른쪽, 짝수일 때는 왼쪽으로 탐사하면서 최댓값을 갱신해주어야 하는 것이 중요하다!
import sys
from collections import deque

def solve():
    tmp = [[0] * (m+2) for i in range(n+2)]
    for i in range(2, n+1):
        tmp[0][0] = dp[i - 1][1]
        for j in range(1, m+1):            
            tmp[0][j] = max(tmp[0][j - 1], dp[i - 1][j]) + board[i][j]
        tmp[1][m + 1] = dp[i - 1][m]
        for j in range(m, 0, -1) :
            tmp[1][j] = max(tmp[1][j + 1], dp[i - 1][j]) + board[i][j]
        for j in range(1, m+1) :
            dp[i][j] = max(tmp[0][j], tmp[1][j])
    return dp[n][m]

n, m = map(int, sys.stdin.readline().strip().split())
board = [[0] * (m+1) for i in range(n+1)]
dp = [[0] * (m+1) for i in range(n+1)]
visited = [[0] * (m+1) for i in range(n+1)]
for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(1, m+1):
        board[i][j] = temp[j-1]
dp[1][1] = board[1][1]
for i in range(2, m+1):
     dp[1][i] = dp[1][i-1] + board[1][i]
print(solve())