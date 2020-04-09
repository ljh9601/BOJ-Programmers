# 풀이일자 : 2020/04/09
# 문제 이름 : 점프 점프
# 문제 번호 : 11060
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 점프의 최소 횟수
# DP의 정의 : n번째 칸까지의 최소 점프 횟수
import sys

n = int(sys.stdin.readline().strip())

maze = [0] * (n+1)
maze[1:] = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (n+1)
for i in range(2, n+1) :
    temp = []
    for j in range(1, i):
        if j + maze[j] >= i and maze[j] > 0 :
            temp.append(dp[j])
    if not temp:
        break
    else :
        dp[i] = min(temp) + 1
if n == 1 :
    print(0)
elif n > 1 :
    print(dp[-1] if dp[-1] > 0 else -1)

# dp[0] = 0
# dp[1] = 0
# dp[2] = 1
# dp[3] = 2
# dp[4] = 2
# dp[5] = 3
# dp[6] = 4
# dp[7] = min(dp[5], dp[6]) + 1 = 4
# dp[8] = min(dp[5], dp[6], dp[7]) + 1 = 4
# dp[9] = dp[8] + 1 = 5
# dp[10] = min(dp[8], dp[9]) + 1 = 5

# dp[9] = 
# dp[10] = min(dp[8], dp[9]) + 1 -> i + maze[8] = 13 > 10 and i + maze[9] = 14 > 10

# 10
# 1 2 0 1 3 2 1 5 4 2