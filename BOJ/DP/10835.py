# 풀이일자 : 2020/05/01
# 문제 이름 : 카드게임
# 문제 번호 : 10835
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
left = deque()
temp = list(map(int, sys.stdin.readline().strip().split()))
for i in temp :
    left.appendleft(i)
right = deque()
temp = list(map(int, sys.stdin.readline().strip().split()))
for i in temp :
    right.appendleft(i)
dp = [[0] * (len(left) + 1) for _ in range(len(right) + 1)]

for i in range(1, len(right)+1) :
    for j in range(1, len(left)+1) :
        dp[i][j] = dp[i-1][j] + right[i-1] if left[j-1] > right[i-1] else max(dp[i-1][j-1], dp[i][j-1])

print(dp[len(right)][len(left)])