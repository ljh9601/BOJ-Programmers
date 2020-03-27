from copy import deepcopy
from collections import deque

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

def move(board, direction, n): 
    merged = [[True] * n for i in range(n)]
    if direction in [0, 3]: 
        start, end, step = 0, n, 1
    else: 
        start, end, step = n-1, -1, -1 

    for i in range(start, end, step): 
        for j in range(start, end, step): 
            if board[i][j] == 0: 
                continue 
            x, y = i, j 
            temp = board[x][y] 
            board[x][y] = 0 
            ax = x + dx[direction]
            ay = y + dy[direction]
            while True: 
                if ax < 0 or ax >= n or ay < 0 or ay >= n: 
                    break 
                if board[ax][ay] == 0: 
                    x, y = ax, ay 
                    ax = x + dx[direction]
                    ay = y + dy[direction] 
                elif board[ax][ay] == temp and merged[ax][ay]: 
                    x, y = ax, ay 
                    merged[x][y] = False 
                    break 
                else: 
                    break 
            board[x][y] = board[x][y] + temp
    return board


def bfs(board, n):
    queue = deque([board]) 
    max_value = -1000000
    count = 0 
    while queue: 
        size = len(queue)
        for idx in range(0, size): 
            board = queue.popleft() 
            for direction in range(0, 4): 
                board_next = move(deepcopy(board), direction, n) 
                queue.append(board_next) 
                for i in range(n): 
                    for j in range(n): 
                        if board_next[i][j] > max_value: 
                            max_value = board_next[i][j] 
        count += 1
        if count == 5: 
            return max_value

if __name__ == "__main__":
    n = int(input())
    count = 0
    result = []
    visited = [[False] * n for i in range(n)]
    board = [[0] * n for i in range(n)]
    for i in range(0, n):
        inputs = list(map(int, input().split()))
        board[i] = inputs
    
    print(bfs(board, n))