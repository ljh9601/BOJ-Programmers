# 풀이일자 : 2020/04/02
# 문제 이름 : Generations of Tribbles
# 문제 번호 : 9507
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 꿈 피보나치값
# dp의 정의 : n번째 수까지의 합 dp[i] = dp[i-1] - dp[n-4] + n
import sys
tcNum = int(sys.stdin.readline().strip())
result = [0] * tcNum
dp = [0] * 69
inputs = [0] * tcNum
for i in range(tcNum):
    inputs[i] = int(sys.stdin.readline().strip())
dp[4] = 8
for i in range(0, max(inputs)+1):
    if i < 2 : 
        dp[i] = 1
        continue
    if i == 2 :
        dp[i] = 2
        continue
    if i == 3 :
        dp[i] = 4
        continue
    elif i > 4:
        dp[i] = dp[i-1] * 2 - dp[i-5]
for i in range(0, tcNum):
    print(dp[inputs[i]])