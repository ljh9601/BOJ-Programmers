import sys
from collections import deque
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(n, board, protection):
    q = []
    curProt = protection - board[0][0]
    visited = [[False] * n for _ in range(n)]
    heapq.heapify(q)
    heapq.heappush(q, (-curProt, start[0], start[1]))

    visited[0][0] = True
    while q:
        curProt, x, y = heapq.heappop(q)
        if x == n-1 and y == n - 1:
            return -curProt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] : 
                    heapq.heappush(q, (curProt + board[nx][ny], nx, ny))
                    visited[nx][ny] = True
    return -1

# 입력
n, protection = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
start = (0,0)
end = (n-1, n-1)
print(bfs(n, board, protection))
