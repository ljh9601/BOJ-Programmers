# 풀이일자 : 2020/03/29
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍 
# 가장 큰 정사각형의 크기
# dp의 정의 : (i, i)에서 만들 수 있는 가장 큰 정사각형의 크기
# 예제에서 dp[1][1] = 4

import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [[0] * m for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * (m+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(i, m):
