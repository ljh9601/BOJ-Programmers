import sys
from copy import deepcopy
maxVal = 4

def setLadder(adj):
    for i in range(n):
        k = i
        for j in range(h):
            if adj[j][k] == 1:
                k += 1
            elif k > 0 and adj[j][k-1] == 1:
                k -= 1
        if i != k:
            return False
    return True

def solve(adj, cnt, x, y):
    global maxVal
    if cnt >= maxVal:
        return
    if setLadder(adj) == True :
        maxVal = min(maxVal, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, h):
        if i == x :
            k = y
        else :
            k = 0
        for j in range(k, n-1):
            if adj[i][j] == 1:
                j += 1
            else:
                adj[i][j] = 1
                solve(adj, cnt+1, i, j+2)
                adj[i][j] = 0

if __name__ == "__main__":
    n, m, h = list(map(int, sys.stdin.readline().strip().split()))
    adj = [[0] * (n+1) for i in range(h+1)]
    for i in range(m):
        x, y = list(map(int, sys.stdin.readline().strip().split()))
        adj[x-1][y-1] = 1
    solve(deepcopy(adj), 0, 0, 0)

if maxVal > 3 :
    print(-1)
else :
    print(maxVal)