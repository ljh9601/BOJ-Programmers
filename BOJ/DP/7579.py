# 풀이일자 : 2020/04/22
# 문제 이름 : 앱
# 문제 번호 : 7579
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 필요한 메모리 M 바이트를 확보하기 위한 앱 비활성화의 최소의 비용
# DP의 정의 : i번째 앱까지 중 j코스트로 얻을 수 있는 최대 바이트 수
import sys

n, m = map(int, sys.stdin.readline().strip().split())
additionalCost = []
byteCost = list(map(int, sys.stdin.readline().strip().split()))
additionalCost = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * (sum(additionalCost) + 1) for _ in range(n+1)]
ans = sys.maxsize

for i in range(1, n+1) :
    for j in range(1, sum(additionalCost) + 1) :
        if j < additionalCost[i-1]:
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], byteCost[i-1] + dp[i-1][j-additionalCost[i-1]])
        if dp[i][j] >= m :
            ans = min(ans, j)
print(ans)