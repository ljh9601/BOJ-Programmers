# 풀이일자 : 2020/04/16
# 문제 이름 : 텀 프로젝트
# 문제 번호 : 9466
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 어느 프로젝트 팀에도 속하지 않는 학생들의 수
# 싸이클을 이루지 않는 학생 수를 구하면 됨!
import sys
from collections import deque

team = []

def dfs(start):
    global team
    cycle = []
    stack = deque()
    stack.appendleft(start)
    while stack :
        current = stack.pop()
        visited[current] = True
        nextIt = choice[current]
        cycle.append(current)
        if not visited[nextIt] :
            stack.append(nextIt)
        else :
            if nextIt in cycle :
                team += cycle[cycle.index(nextIt):]

tcNum = int(sys.stdin.readline().strip())
for _ in range(tcNum):
    n = int(sys.stdin.readline().strip())
    team = []
    visited = [False] * (n+1)
    choice = [0] + list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    print(n - len(team))