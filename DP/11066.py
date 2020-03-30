# 풀이일자 : 2020/03/30
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍 
# 파일을 합치는 최소비용
# dp의 정의 : 1~n장까지 합쳤을 때의 최소비용
# 유의사항 : Knuth Optimization 을 활용한 최적화 -> O(n^3) 에서 O(n^2)로 최적화 가능

# Knuth Optimization은 다음조건 아래에서만 사용될 수 있다.

# 조건 0) dp[i][j] 는1 ≤ i ≤ j ≤ n 일 때만 정의된다.
# 조건 1) dp[i][j] = min(dp[i][k]+dp[k+1][j]) + cost[i][j] 
# 조건 2) (사각 부등식)
    # a ≤ b ≤ c ≤ d 일 때,
    # cost[a][c] + cost[b][d] ≤ cost[a][d] + cost[b][c]
# 조건 3) (구간 단조성)
# a ≤ b ≤ c ≤ d 일 때,
# cost[b][c] ≤ cost[a][d]

import sys
 
n = int(sys.stdin.readline().strip())
result = []

for i in range(n):
    num = int(sys.stdin.readline().strip())
    files = list(map(int, sys.stdin.readline().strip().split()))
    dp = [[0] * num for _ in range(num)]
    sumVal = [0] * (num+1)

    sumVal[1] = files[0]
    for j in range(1, num+1):
        sumVal[j] = sumVal[j-1] + files[j-1]
 
    knuth = [[0 for _ in range(num)] for _ in range(num)]
    for j in range(num):
        knuth[j][j]=j
 
    for j in range(1,num):
        for k in range(num-j):
            temp = j + k
            dp[k][temp] = 999999999999
            for l in range (knuth[k][temp-1], knuth[k+1][temp] + 1):
                if l < num - 1 and dp[k][temp] > dp[k][l] + dp[l+1][temp] + sumVal[temp+1] - sumVal[k]:
                    dp[k][temp] = dp[k][l] + dp[l+1][temp] + sumVal[temp+1] - sumVal[k]
                    knuth[k][temp] = l
        if dp[0][num-1] > 0:
            result.append(dp[0][num-1])
for i in result:
    print(i)