# 풀이일자 : 2020/05/07
# 문제 이름 : 불!
# 문제 번호 : 4179
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS, DFS
# 지훈이가 미로를 탈출하는 최소 시간
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start) :
    q = deque()
    q.appendleft(start)
    visited[start[0]][start[1]] = 1
    while q :
        fireLength = len(firePos)
        for _ in range(fireLength):
            fireX, fireY = firePos.popleft()
            for i in range(4):
                nFireX = fireX + dx[i]
                nFireY = fireY + dy[i]
                if 0 <= nFireX < r and 0 <= nFireY < c :
                    if not visited[nFireX][nFireY] and board[nFireX][nFireY] == '.' :
                        board[nFireX][nFireY] = 'F'
                        firePos.append((nFireX, nFireY))
        qLen = len(q)
        for _ in range(qLen):
            x, y = q.popleft()
            if x == 0 or y == 0 or x == r-1 or y == c-1 :
                return visited[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c :
                    if not visited[nx][ny] and board[nx][ny] == '.' :
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    return 0

r, c = map(int, sys.stdin.readline().strip().split())
board = [['0'] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]
firePos = deque()
for i in range(r):
    board[i] = list(map(str, sys.stdin.readline().strip()))
    for j in range(c):
        if board[i][j] == 'J' :
            startPos = (i, j)
        if board[i][j] == 'F' :
            firePos.append((i, j))
ans = bfs(startPos)
print(ans if ans > 0 else 'IMPOSSIBLE')