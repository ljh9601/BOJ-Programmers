# 풀이일자 : 2020/05/05
# 문제 이름 : 말이 되고픈 원숭이
# 문제 번호 : 1600
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 원숭이의 최소 동작수
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

dxHorse = [-2, -1, 1, 2, -2, -1, 1, 2]
dyHorse = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(end, k) :
    q = deque()
    q.appendleft((0, 0, k, 0))
    visited[k][0][0] = True
    while q :
        x, y, k, ans = q.popleft()
        if x == end[0] and y == end[1] :
            return ans
        if k > 0 :
            for i in range(8):
                nHorseX = x + dxHorse[i]
                nHorseY = y + dyHorse[i]
                if 0 <= nHorseX < h and 0 <= nHorseY < w :
                    if not visited[k-1][nHorseX][nHorseY] and not board[nHorseX][nHorseY] :
                        visited[k-1][nHorseX][nHorseY] = True
                        q.append((nHorseX, nHorseY, k-1, ans + 1))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w :
                if not visited[k][nx][ny] and not board[nx][ny] :
                    visited[k][nx][ny] = True
                    q.append((nx, ny, k, ans + 1))

    return -1

k = int(sys.stdin.readline().strip())
w, h = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for __ in range(h)]
visited = [[[False] * w for _ in range(h)] for __ in range(k+1)]
end = (h-1, w-1)
print(bfs(end, k))