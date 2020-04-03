# 풀이일자 : 2020/04/03
# 문제 이름 : 외판원 순회
# 문제 번호 : 2098
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 가장 적은 비용을 들이는 외판원의 순회 여행 경로
# dp의 정의 : 
import sys
maxVal = 100000000
def solve(current, visited) :
    #모든 도시 방문
    if visited == (1 << n) - 1 :
        if arr[current][0] != 0 :
            return arr[current][0] or maxVal
    if dp[current][visited] != -1:
        return dp[current][visited]
    minVal = maxVal
    for i in range(n):
        # 아직 방문하지 않았다면
        if not (visited & (1 << i)) and arr[current][i] :
            minVal = min(minVal, solve(i, visited | (1<<i)) + arr[current][i])
    dp[current][visited] = minVal
    return minVal

n = int(sys.stdin.readline().strip())
arr = [[0] * (n+1) for i in range(n+1)]
dp = [[-1] * (1 << (n)) for i in range(n+1)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))
print(solve(0, 1))