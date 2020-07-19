# 풀이일자 : 2020/04/28
# 문제 이름 : 숫자고르기
# 문제 번호 : 2668
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 뽑힌 정수들
import sys
from collections import deque

def dfs(start):
    stack = deque()
    cycle = [start]
    visited[start] = True
    stack.appendleft(start)
    while stack :
        current = stack.pop()
        if arr[current] == start :
            return cycle
        if visited[arr[current]] == 0 and arr[current] not in cycle:
            cycle.append(arr[current])
            visited[arr[current]] = True
            stack.append(arr[current])
    return []

n = int(sys.stdin.readline().strip())
arr = [0] * (n+1)
for i in range(n):
    arr[i+1] = int(sys.stdin.readline().strip())
ans = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    temp = dfs(i)
    for j in temp :
        if j not in ans :
            ans.append(j)
print(len(ans))
for i in sorted(ans) :
    print(i)