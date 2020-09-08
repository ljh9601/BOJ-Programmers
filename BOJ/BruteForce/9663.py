import sys

def dfs(idx):
    if idx == n :
        return ans.append(board)
    
    for col in range(n):
        if row[col] + left[idx+col] + right[n-1+idx-col]==0:
            row[col]=left[idx+col]=right[n-1+idx-col]=1
            dfs(idx+1)
            row[col]= left[idx+col]= right[n-1+idx-col] = 0

n = int(sys.stdin.readline().strip())
board = [[False] * n for _ in range(n)]
ans = []
row,left,right=[0] * n, [0] * (2 * n - 1),[0] * (2 * n - 1)
dfs(0)
print(len(ans))