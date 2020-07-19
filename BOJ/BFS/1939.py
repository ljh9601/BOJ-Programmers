# 풀이일자 : 2020/05/06
# 문제 이름 : 중량 제한
# 문제 번호 : 1939
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 한 번의 이동으로 옮길 수 있는 최대의 물품 수량
# 이분 탐색 + BFS로 최대 중량을 구하면 된다.
# 이분 탐색을 사용하는 이유는 가능한 경로에서 최대의 중량을 구하기 위함!
import sys
from collections import deque

_min, _max = 1, 1000000000

def bfs(mid):
    q = deque()
    q.append(start)
    visited = []
    visited.append(start)
    while q :
        current = q.popleft()
        for bridge, weigh in board[current] :
            if bridge not in visited and weigh >= mid:
                visited.append(bridge)
                q.append(bridge)
    return True if end in visited else False

n, m = map(int, sys.stdin.readline().strip().split())
board = [[] for _ in range(n+1)]
for i in range(m):
    x, y, weight = map(int, sys.stdin.readline().strip().split())
    board[x].append([y, weight])
    board[y].append([x, weight])
start, end = map(int, sys.stdin.readline().strip().split())

result = _min
while _min <= _max :
    mid = (_min + _max) // 2
    if bfs(mid) :
        result = mid
        _min = mid + 1
    else :
        _max = mid - 1
print(result)