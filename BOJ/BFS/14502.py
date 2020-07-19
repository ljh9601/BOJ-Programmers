from copy import deepcopy
from collections import deque
import sys

def bfs(arr, visited, start, n, m):
    visited[start[0]][start[1]] = True
    queue = deque()
    queue.append(start)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue :
        x, y = queue.popleft()
        for i in range(0, 4):
            ax = x + dx[i]
            ay = y + dy[i]
            if ax >= 0 and ax < n and ay >= 0 and ay < m:
                if not visited[ax][ay] and arr[ax][ay] is 0 :
                    visited[ax][ay] = True
                    arr[ax][ay] = 2
                    queue.append((ax, ay))


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    arr = [[0] * m for i in range(n)]
    wall = []
    result = []
    
    for i in range(n):
        inputs = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(m):
            arr[i][j] = inputs[j]
            if arr[i][j] is 0 :
                wall.append((i, j))
    
    for i in range(0, len(wall)-2):
        for j in range(i+1, len(wall)-1):
            for k in range(j+1, len(wall)):
                visited = [[0] * m for i in range(n)]
                
                count = 0
                
                aWall = wall[i]
                bWall = wall[j]
                cWall = wall[k]

                tempMap = deepcopy(arr)
                tempMap[aWall[0]][aWall[1]] = 1
                tempMap[bWall[0]][bWall[1]] = 1
                tempMap[cWall[0]][cWall[1]] = 1

                for idx in range(0, n):
                    for idx_ in range(0, m):
                        if tempMap[idx][idx_] is 2 :
                            start = (idx, idx_)
                            bfs(tempMap, visited, start, n, m)
                for idx in range(0, n):
                    for idx_ in range(0, m):
                        if tempMap[idx][idx_] is 0 :
                            count += 1
                result.append(count)
    print(max(result))