from collections import deque

#상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

snake = deque([(1,1)])

def move(board, direction, n):    
    (x, y) = snake[0]
    ax = x + dx[direction]
    ay = y + dy[direction]

    if (ax, ay) in snake :
        return -1
    if ax <= 0 or ax > n or ay <= 0 or ay > n :
        return -1
    if board[ax][ay] == 0:
        (tailX, tailY) = snake.pop()
        board[tailX][tailY] = 0
    
    board[ax][ay] = 1
    snake.appendleft((ax, ay))

    return 0
    
def rotate(howToMove, current):
    # D : 상 -> 우(dx[0] -> dx[1]), 우 -> 하(dx[1] -> dx[2]), 하 -> 좌 (dx[2] -> dx[3]), 좌 -> 상(dx[3] -> dx[0])  => (i + 1) % 4
    # L : 상 -> 좌(dx[0] -> dx[3]), 우 -> 상(dx[1] -> dx[0]), 하 -> 우(dx[2] -> dx[1]), 좌 -> 하(dx[3] -> dx[2]) => (i + 3) % 4
    if howToMove == 'D':
        return (current + 1) % 4
    else :
        return (current + 3) % 4

def solve(board, trans, n):
    time = 0
    index = 0
    direction = 1

    while True :
        if index < len(trans) and trans[index][0] == time :
            direction = rotate(trans[index][1], direction)
            index += 1
        if move(board, direction, n) == -1 :
            print(time + 1)
            return

        time += 1

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    board = [[0] * (n+1) for i in range (n+1)]
    apples = [[0] * 2 for i in range(m)]
    count = 0
    start = (0, 0)

    for i in range(0, m):
        apples[i] = list(map(int, input().split()))
        board[apples[i][0]][apples[i][1]] = -2

    v = int(input())
    trans = [['0'] * 2 for i in range(v)]

    for i in range(0, v):
        sec, howToMove = input().split()
        trans[i][0] = int(sec)
        trans[i][1] = howToMove
    board[1][1] = 1
    solve(board, trans, n)
    