# 풀이일자 : 2020/05/09
# 문제 이름 : 사회망 서비스(SNS)
# 문제 번호 : 2533
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# DP의 정의 : dp[i][j] : i번 사람이 얼리어답터일 때, 혹은 얼리어답터가 아닐 때 i번 사람 하위 노드까지의 최소 얼리 어답터 수
# 이 문제는 특이하게 PyPy3 로 채점할 경우 메모리 초과가 뜨고, python3로 채점할 경우 아슬아슬하게 통과되었다.
# 이유를 추측해보자면 PyPy3가 성능 면에서 뛰어난 대신 본질적으로 메모리 사용량이 더 많은 것을 보인다. 시간 개선을 위해 메모리 사용량의 최적화를 일부 포기한 것 아닐까 추측해본다.
import sys
sys.setrecursionlimit(1000000000)

def solve(start):
    visited[start] = True
    dp[start][0] = 1
    dp[start][1] = 0
    for i in inputs[start]:
        if not visited[i] :
            solve(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][0], dp[i][1])

n = int(sys.stdin.readline().strip())
inputs = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dp = [[0,0] for _ in range(n+1)]
for i in range(0, n-1) :
    parent, child = map(int, sys.stdin.readline().strip().split())
    inputs[parent].append(child)
    inputs[child].append(parent)
solve(1)
print(n - max(dp[1]))