# 풀이일자 : 2020/05/09
# 문제 이름 : 사회망 서비스(SNS)
# 문제 번호 : 2533
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# DP의 정의 : dp[i][j] : i번 사람이 얼리어답터일 때, 혹은 얼리어답터가 아닐 때 i번 사람 하위 노드까지의 최소 얼리 어답터 수
import sys
from collections import deque

def dfs(start):
    stack = deque()
    stack.append(start)
    while stack :
        current = stack.pop()
        for item in 

n = int(sys.stdin.readline().strip())
inputs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [0] * 
for i in range(1, n+1):
    dfs(i)