# 풀이일자 : 2020/04/01
# 문제 이름 : 펠린드롬?
# 문제 번호 : 10942
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 명우의 대답
# dp의 정의 : n,m에서의 펠린드롬을 미리 구한다. 다만 구할 때 이전의 dp값을 활용해야 시간초과를 막을 수 있다.
import sys

n = int(sys.stdin.readline().strip())
nums = [0] * n
nums = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
question = [[0] * 2 for i in range(m)]
ans = [0] * m
dp = [[0] * (n) for i in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1
for i in range(2, n):
    for j in range(n-i):
        if nums[j] == nums[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    print(dp[a - 1][b - 1])