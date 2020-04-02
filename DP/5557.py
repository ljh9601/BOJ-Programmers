# 풀이일자 : 2020/04/02
# 문제 이름 : 1학년
# 문제 번호 : 5557
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 만들 수 있는 등식의 개수
# dp의 정의 : 트리처럼 더하고 빼는 것을 반복하며 그때까지의 합 혹은 차의 값 인덱스에 연산횟수 저장
# ex) dp[1][5] = 1, dp[1][11] = 1
import sys
n = int(sys.stdin.readline().strip())
inputs = [0] * n
inputs = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * 21 for i in range(n)]
dp[0][inputs[0]] = 1
for i in range(1, n-1):
    for j in range(21):
        if j + inputs[i] <= 20 :
            dp[i][j + inputs[i]] += dp[i-1][j]
        if j - inputs[i] >= 0 :
            dp[i][j - inputs[i]] += dp[i-1][j]
print(dp[n-2][inputs[n-1]])