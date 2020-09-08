import sys
from collections import defaultdict

# 칸 번호, 해당 칸의 점수, 해당 칸의 화살표들
# 빨간색 : 'red', 파란색 : 'blue'
INF = 987654321
special = [10, 20, 30]
dice = list(map(int, sys.stdin.readline().strip().split()))
board = defaultdict(list)
board[0] = [(1, 2)]
for i in range(19):
    board[i+1].append((i+2, (i+2)*2))
gridNum = 20
for num in special :
    current = num // 2
    curPoint = num
    if num == 10 :
        for i in range(3):
            board[current].append((gridNum, curPoint + 3))
            curPoint += 3
            current = gridNum
            gridNum += 1
        board[gridNum - 1].append((28, 25))
        gridNum = 23
    if num == 20 :
        for i in range(2):
            board[current].append((gridNum, curPoint + 2))
            current = gridNum
            curPoint += 2
            gridNum += 1
        board[gridNum - 1].append((28, 25))
        gridNum = 25
    if num == 30 :
        current = num // 2
        standard = 15
        gridNum = 25
        board[standard].append((gridNum, 28))
        current += 1
        board[gridNum].append((gridNum + 1, 27))
        current += 1
        gridNum += 1
        board[gridNum].append((gridNum + 1, 26))
        gridNum += 1
        board[gridNum].append((28, 25))
        gridNum = 29
gridNum = 29
curP = 30
for i in range(3):
    board[gridNum - 1].append((gridNum, curP))
    gridNum += 1
    curP += 5
board[31] = [(INF, INF)]
for i in range(len(board)):
    print(i, board[i])


