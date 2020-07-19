# 풀이일자 : 2020/05/08
# 문제 이름 : 구슬 찾기
# 문제 번호 : 2617
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
import sys
from collections import deque

def dfsHeavy(start):
    global ans
    stack = deque()
    visited = [False] * (n+1)
    stack.appendleft(start)
    visited[start] = True
    count = 0
    while stack :
        current = stack.pop()
        for item in relationHeavy[current] :
            if not visited[item] :
                count += 1
                visited[item] = True
                if count > boundary :
                    ans += 1
                    return
                stack.append(item)

def dfsLight(start):
    global ans
    stack = deque()
    visited = [False] * (n+1)
    stack.appendleft(start)
    visited[start] = True
    count = 0
    while stack :
        current = stack.pop()
        for item in relationLight[current] :
            if not visited[item] :
                count += 1
                visited[item] = True
                if count > boundary :
                    ans += 1
                    return
                stack.append(item)

n, m = map(int, sys.stdin.readline().strip().split())
boundary = n // 2
relationHeavy = [[] for _ in range(n+1)] # 자기 자신보다 무거운 구슬들을 저장
relationLight = [[] for _ in range(n+1)]
ans = 0
for _ in range(m):
    heavy, light = map(int, sys.stdin.readline().strip().split())
    relationHeavy[light].append(heavy)
    relationLight[heavy].append(light)
for i in range(1, n+1):
    dfsHeavy(i)
    dfsLight(i)
print(ans)
# 1 -> 2, 5
# 2 -> 1, 4
# 3 -> 4
# 4 -> 2, 3
# 5 -> 1

# 1 -> 2, 5
# 2 -> 4
# 3 -> 4
# 4 -> 
# 5 -> 