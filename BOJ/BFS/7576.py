from collections import deque

def isInside(y,x):
    return (0<= y <N) and (0<= x <M)

def BFS():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i] 
            if isInside(ny, nx):
                # 이웃한 토마토가 아직 익지 않았다면 해당 값은 0 일 것. 
                if not tomato[ny][nx]:
                    queue.append([ny,nx])
                    tomato[ny][nx] = tomato[y][x] + 1

def Solve():
    res = 0
    for i in range(N):
        if 0 in tomato[i]:
            return -1
        res = max(res, max(tomato[i]))
    return (res - 1)

M, N = map(int, input().split())
queue = deque()
tomato = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        if tomato[i][j] is 1:
            queue.append([i, j])

BFS()
print(Solve())