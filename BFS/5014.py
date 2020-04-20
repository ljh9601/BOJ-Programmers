# 풀이일자 : 2020/04/20
# 문제 이름 : 스타트링크
# 문제 번호 : 5014
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 눌러야 하는 버튼의 총 개수
import sys
from collections import deque

def bfs(start):
    dx = [u, -d]
    q = deque()
    q.appendleft(start)
    if start == g :
        return 1
    while q :
        current = q.popleft()
        if current == g :
            break
        for i in range(2):
            nxt = current + dx[i]
            if 0 < nxt <= f :
                if not visited[nxt] and nxt != s:
                    visited[nxt] = visited[current] + 1
                    q.append(nxt)
    return visited[g]


f, s, g, u, d = map(int, sys.stdin.readline().strip().split())
visited = [0] * (f+1)
visited[s] = 1
if (u == 0 and g - s > 0) or (d == 0 and g - s < 0) :
    print('use the stairs')
    exit()
ans = bfs(s)
print((ans - 1) if ans > 0 else 'use the stairs')