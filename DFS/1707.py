# 풀이일자 : 2020/04/09
# 문제 이름 : 이분 그래프
# 문제 번호 : 1707
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 이분그래프인지 아닌지 판별.
import sys
from collections import deque
cnt = 0

def dfs(pos):
    global cnt
    stack = deque()
    stack.appendleft(pos)
    while stack :
        current = stack.pop()
        if visited[current] :
            continue
        if not visited[current] :
            cnt = 2 if cnt == 1 else 1
            visited[current] = cnt
        for i in path[current]:
            if visited[i] != 0 and visited[i] % 2 == current % 2 :
                return False
        for i in path.keys() :
            temp = i
            if i!= 1:
                temp = len(path[i-1])-path[i-1][current] + path[i][current]
            if not visited[temp] :
                stack.append(i)
    return True

tcNum = int(sys.stdin.readline().strip())
for i in range(tcNum):
    path = {}
    v, e = map(int, sys.stdin.readline().strip().split())
    visited = [0] * (v+1)
    for j in range(e):
        start, end = map(int, sys.stdin.readline().strip().split())
        if start not in path :
            path[start] = set([])
        if end not in path :
            path[end] = set([])
        path[start].add(end)
    print('YES' if dfs(1) else 'NO')