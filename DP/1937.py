# DFS를 이용한 각 인덱스별 탐색
# dp의 정의 : 입력한 배열과 크기를 똑같이 선언하고, 각 값마다 그 값에서 최대한 생존할 수 있는 일수를 저장.
# 시간초과가 날 것 같지만, 증가하는 방향이라는 점 때문에 연산 횟수가 크게 줄어들 것.
import sys
sys.setrecursionlimit(50000)

dx = [-1 ,1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

n = int(sys.stdin.readline().strip())
assert 0 < n <= 1000000
arr = [[0] * n for i in range(n)]
dp = [[0] * n for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))
maxVal = dp[0][0]

for i in range(n):
    for j in range(n):
        dp[i][j] = dfs(i, j)

for i in range(n):
    for j in range(n):
        if maxVal < dp[i][j]:
            maxVal = dp[i][j]

print(maxVal)