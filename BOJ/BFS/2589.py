# 풀이일자 : 2020/04/16
# 문제 이름 : 보물섬
# 문제 번호 : 2589
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 보물이 묻혀 있는 두 지점 간의 최소 거리
# 완전 탐색을 통한 BFS로 풀면 된다.
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(posX, posY):
    q = deque()
    q.appendleft((posX, posY))
    visited = [[0] * m for i in range(n)]
    count = 0
    visited[posX][posY] = 1
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and board[nx][ny] == 'L' :
                    visited[nx][ny] = visited[x][y] + 1
                    count = max(count, visited[nx][ny])
                    q.append((nx, ny))
    return count - 1

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(map(str, sys.stdin.readline().strip())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L' :
            ans = max(ans, bfs(i, j))
print(ans)