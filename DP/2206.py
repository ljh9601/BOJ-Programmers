# 풀이일자 : 2020/04/10
# 문제 이름 : 벽 부수고 이동하기
# 문제 번호 : 2206
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 주어진 맵에서의 최단 경로
# 탐색을 하며 장애물을 파괴할 때 그 전까지의 visited 배열을 저장하고, 파괴할 경우 및 파괴하지 않을 경우를 함께 BFS해야 시간초과를 막을 수 있다.
import sys
from copy import deepcopy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(posX, posY, isDestroyed, distance):
    q = deque()
    q.appendleft([posX, posY, isDestroyed, distance])
    while q :
        x, y, nIsDestroyed, dist = q.popleft()
        if x == n-1 and y == m-1 :
            return dist
        dist += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if not board[nx][ny] and not visited[nIsDestroyed][nx][ny] :
                    visited[0][nx][ny] = True
                    if nIsDestroyed :
                        visited[1][nx][ny] = True
                    q.append((nx, ny, nIsDestroyed, dist))
                elif nIsDestroyed and board[nx][ny] :
                    visited[0][nx][ny] = True
                    q.append((nx, ny, 0, dist))
    return -1

n, m = map(int, sys.stdin.readline().strip().split())
board = [[0] * m for i in range(n)]
visited = [[[False] * m for _ in range(n)] for i in range(2)]
result = []
for i in range(n):
    board[i] = list(map(str, sys.stdin.readline().strip()))
for i in range(n):
    for j in range(m):
        board[i][j] = int(board[i][j])
print(bfs(0, 0, 1, 1))