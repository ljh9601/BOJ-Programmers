# 풀이일자 : 2020/05/06
# 문제 이름 : 경찰차
# 문제 번호 : 2618
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 두 대의 경찰차가 이동하는 거리의 합의 최솟값
# dp의 정의 : dp[i][j] : 경찰차1이 마지막으로 해결한 i번째 사건, 경찰차2가 마지막으로 해결한 j번째 사건까지의 이동 거리의 최솟값
# 결국 시간초과로 Solve 실패.. 후에 다시 풀어볼 것.
import sys

def dist (a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(x, y) :
    nextIncident = max(x, y) + 1
    if nextIncident == w+2 :
        return 0
    ans = dp[x][y]
    if ans != -1 :
        return ans
    
    ans = solve(nextIncident, y) + dist(incidents[x], incidents[nextIncident])
    elseCase = solve(x, nextIncident) + dist(incidents[y], incidents[nextIncident])
    
    if elseCase < ans :
        ans = elseCase
        choose[x][y] = 1
    
    return ans

n = int(sys.stdin.readline().strip())
w = int(sys.stdin.readline().strip())

incidents = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(w)]
incidents.insert(0, [1, 1])
incidents.insert(1, [n, n])
dp = [[-1] * (w+1) for i in range(w+1)]
choose = [[0] * (w+1) for i in range(w+1)]
print(solve(0, 1))
x = 0
y = 1
while max(x, y)+1 < w+2 :
    print(choose[x][y] + 1)
    if choose[x][y] :
        y = max(x, y) + 1
    else :
        x = max(x, y) + 1