# 풀이일자 : 2020/04/23
# 문제 이름 : 상범 빌딩
# 문제 번호 : 6593
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 탈출이 가능한지에 대한 여부
import sys
from collections import deque
#동서남북상하
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]][start[2]] = 0
    while q :
        x, y, z = q.popleft()
        if building[x][y][z] == 'E':
            return visited[x][y][z]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if visited[nx][ny][nz] == -1 and (building[nx][ny][nz] == '.' or building[nx][ny][nz] == 'E'):
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append((nx, ny, nz))
    return 0

while True :
    l, r, c = map(int, sys.stdin.readline().strip().split())
    if not l and not r and not c :
        exit()
    building = [[['0'] * c for _ in range(r)] for __ in range(l)]
    visited = [[[-1] * c for _ in range(r)] for __ in range(l)]
    count = 0

    for i in range(l):
        building[i] = [list(input().strip()) for _ in range(r)]
        input()
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    start = (i, j, k)
                if building[i][j][k] == 'E':
                    end = (i, j, k)

    ans = bfs(start, end)
    print('Escaped in ' + str(ans) +' minute(s).' if ans > 0 else 'Trapped!')