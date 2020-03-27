import sys
from copy import deepcopy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(arr, visited, result, start, sumVal, count):
    if count == 4 :
        result.append(sumVal)
        return

    x, y = start[0], start[1]
    for i in range(0, 4):
        ax = x + dx[i]
        ay = y + dy[i]
        if ax >= 0 and ax < n and ay >= 0 and ay < m:
            if visited[ax][ay] is False :
                visited[ax][ay] = True
                start = (ax, ay)
                dfs(arr, visited, result, start, sumVal + arr[ax][ay], count + 1)
                visited[ax][ay] = False

def exceptCase(arr, result, start, n, m) :
    x,y = start[0], start[1]
    sumVal = arr[x][y]
    
    if x == 0:
        if y == 0 or y == m-1:
            return
    elif x == n-1:
        if y == 0 or y == m-1:
            return
 
    if x == 0:
        sumVal += arr[x+1][y] + arr[x][y-1] + arr[x][y+1]
    elif x == n-1: 
        sumVal += arr[x-1][y] + arr[x][y-1] + arr[x][y+1]    
    elif y == 0:
        sumVal += arr[x][y+1] + arr[x-1][y] + arr[x+1][y]    
    elif y == m-1:
        sumVal += arr[x][y-1] + arr[x-1][y] + arr[x+1][y]
    else:
        sumlist = []
        sumlist.append(sumVal + arr[x+1][y] + arr[x][y-1] + arr[x][y+1])
        sumlist.append(sumVal + arr[x-1][y] + arr[x][y-1] + arr[x][y+1])
        sumlist.append(sumVal + arr[x][y+1] + arr[x-1][y] + arr[x+1][y])
        sumlist.append(sumVal + arr[x][y-1] + arr[x-1][y] + arr[x+1][y])
        sumVal = max(sumlist)

    result.append(sumVal)

if __name__ == "__main__":
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    arr = [[0] * m for i in range (n)]
    visited = [[False] * m for i in range (n)]
    result = []
    sumVal = 0
    for i in range(0, n):
        inputs = list(map(int, sys.stdin.readline().strip().split()))
        arr[i] = inputs
    
    for i in range(0, n):
        for j in range(0, m):
            start = (i, j)
            visited[i][j] = True
            exceptCase(arr, result, start, n, m)
            dfs(arr, visited, result, start, arr[i][j], 1)
            visited[i][j] = False

    print(max(result))