# 풀이일자 : 2020/04/16
# 문제 이름 : 텀 프로젝트
# 문제 번호 : 9466
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 어느 프로젝트 팀에도 속하지 않는 학생들의 수
import sys
from collections import deque

def dfs(start):
    stack = deque()
    stack.appendleft(start)
    count = 0
    temp = []
    while stack :
        current = stack.pop()
        if not visited[current] :
            visited[current] = True
        if current not in temp :
            temp.append(current)
        if current in choice[start] :
            temp = [start, current]
        if start in choice[current]:
            count += len(temp)
            return count
        for i in choice[current] :
            if not visited[i] :
                stack.append(i)
    return 0

tcNum = int(sys.stdin.readline().strip())
for _ in range(tcNum):
    n = int(sys.stdin.readline().strip())
    visited = [False] * (n+1)
    choice = [[] for __ in range(n+1)]
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, n+1):
         choice[temp[i-1]].append(i)
    ans = 0
    for i in range(1, n+1):
        if len(choice[i]) > 0 and not visited[i]:
            ans += dfs(i)
    print(n - ans)