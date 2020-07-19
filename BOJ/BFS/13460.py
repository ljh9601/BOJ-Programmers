from collections import deque

def bfs(board, visited, startR, startB):
    count = 1
    queue = deque()
    start = ((startR[0], startR[1], startB[0], startB[1], 1))
    queue.append(start)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        xR, yR, xB, yB, count = queue.popleft()
        if count > 10 :
            break
        for i in range (0, 4):
            axR, ayR, rMoveCnt = move(board, xR, yR, dx[i], dy[i], 0)
            axB, ayB, bMoveCnt = move(board, xB, yB, dx[i], dy[i], 0)            
            if board[axB][ayB] == 'O':
                continue
            if board[axR][ayR] == 'O':
                print(count)
                return
            if axR == axB and ayR == ayB :
                if rMoveCnt > bMoveCnt :
                    axR = axR - dx[i]
                    ayR = ayR - dy[i]
                else :
                    axB = axB - dx[i]
                    ayB = ayB - dy[i]
            if visited[axR][ayR][axB][ayB] == False :
                visited[axR][ayR][axB][ayB] = True
                queue.append((axR, ayR, axB, ayB, count + 1))
    print(-1)
            
def move(board, x, y, dx, dy, moveCnt):
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        moveCnt += 1
    return x, y, moveCnt
        
if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    board = [['0'] * m for i in range(n)]
    visited = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]

    startR = (0, 0)
    startB = (0, 0)
    for i in range(0, n):
        inputs = input()
        for j in range(0, m):
            board[i][j] = inputs[j]
            if inputs[j] == 'R':
                startR = (i, j)
                xR = i
                yR = j
            if inputs[j] == 'B':
                startB = (i, j)
                xB = i
                yB = j
    visited[xR][yR][xB][yB] = True    
    
    bfs(board, visited, startR, startB)
