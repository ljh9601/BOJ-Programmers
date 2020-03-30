# 풀이일자 : 2020/03/29
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍 
# n라운드 진행 후 열려있는 문의 개수
# dp의 정의 : n/2 라운드까지 진행한 후 열려있는 방의 개수 + n/2~n 까지의 방에서 닫혀있는 방의 개수
# ex ) dp[3] : 3라운드가 진행 

# Case when n = 5
# Initial : opened -> x
# After 1round : opened -> 1 2 3 4 5, closed -> x
# After 2round : opened -> 1   3   5, closed -> 2 4
# After 3round : opened -> 1       5, closed -> 2 3 4
# After 4round : opened -> 1     4 5, closed -> 2 3
# After 5round : opened -> 1     4  , closed -> 2 3 5

# Case when n = 10
# Initial : opened -> x
# After 1round : opened -> 1 2 3 4 5 6 7 8 9 10, closed -> x
# After 2round : opened -> 1   3   5   7   9   , closed -> 2 4 6 8 10
# After 3round : opened -> 1       5 6         , closed -> 2 3 4 7 8 9 10
# After 4round : opened -> 1     4 5 6   8     , closed -> 2 3 7 9 10
# After 5round : opened -> 1     4   6   8   10, closed -> 2 3 5 7 9
# After 6round : opened -> 1     4       8   10, closed -> 2 3 5 6 7 9
# After 7round : opened -> 1     4     7 8   10, closed -> 2 3 5 6 9
# After 8round : opened -> 1     4     7     10, closed -> 2 3 5 6 8 9
# After 9round : opened -> 1     4     7   9 10, closed -> 2 3 5 6 8
# After 10round : opened -> 1    4     7   9   , closed -> 2 3 5 6 8 10
#dp[n] = dp[n-1] - count(k의 배수)
import sys

tcNum = int(sys.stdin.readline().strip())
inputs = []
result = []
for i in range(tcNum):
    inputs.append(int(sys.stdin.readline().strip()))

for j in range (0, len(inputs)):
    dp = [0] * (inputs[j])
    for k in range(1, inputs[j]+1):
        for i in range(k-1, inputs[j], k):
            if dp[i] == 0 : 
                dp[i] = 1
            elif dp[i] == 1 : 
                dp[i] = 0
    result.append(dp.count(1))
for i in result:
    print(i)

