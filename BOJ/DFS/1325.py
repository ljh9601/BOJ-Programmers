# 풀이일자 : 2020/04/22
# 문제 이름 : 효율적인 해킹
# 문제 번호 : 1325
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호
import sys
from collections import deque
maxVal = -1

def dfs(start):
    global maxVal
    stack = deque()
    visited = [False] * (n+1)
    visited[start] = True
    stack.appendleft(start)
    count = 1
    while stack :
        current = stack.pop()
        for i in path[current] :
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                count += 1
    return count
n, m = map(int, sys.stdin.readline().strip().split())
path = [[] for i in range(n+1)]
result = []
for i in range(m):
    start, end = map(int, sys.stdin.readline().strip().split())
    path[end].append(start)
for i in range(1, n+1):
    cnt = dfs(i)
    if cnt == maxVal :
        result.append(i)
        maxVal = cnt
    elif cnt > maxVal :
        result = [i]
        maxVal = cnt
for i in result:
    print(i, end=" ")