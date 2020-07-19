import sys

visited = [[False] * 101 for i in range(101)]
        
def rotate(start, condition):
    x, y = start
    d, g = condition

    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    curve = [d]
    for _ in range(g):
        curve += [((i+1)%4) for i in curve[::-1]]
    visited[x][y] = 1
    nx, ny = x, y
    for i in curve:
        nx, ny = nx + dx[i], ny + dy[i]
        if nx >= 0 and nx < 101 and ny >= 0 and ny < 101:
            visited[nx][ny] = 1


if __name__ == "__main__":
    n = int(input())
    count = 0
    rotateInfo = [[0] * 4 for i in range(n)]
    for i in range(0, n):
        y, x, d, g = map(int, sys.stdin.readline().split())
        rotate((x,y), (d,g))
    for i in range(0, 100):
        for j in range(0, 100):
            if visited[i][j] == True and visited[i+1][j] == True and visited[i][j+1] == True and visited[i+1][j+1] == True:
                count += 1
    print(count)