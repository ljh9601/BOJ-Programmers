# 풀이일자 : 2020/04/20
# 문제 이름 : Puyo Puyo
# 문제 번호 : 11559
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 뿌요뿌요 게임의 연쇄 횟수
# 완전탐색이 필수인 문제. 색깔이 칠해진 칸에서 dfs를 돌리며 이동한 칸이 4칸 이상일 경우 '.'으로 바꾼 다음 위에서 당겨오면 된다.
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(posX, posY):
    stack = deque()
    stack.append((posX, posY))
    currentVisited = []
    color = board[posX][posY]
    while stack :
        x, y = stack.pop()
        if (x, y) in currentVisited :
            continue
        currentVisited.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if board[nx][ny] == color:
                    stack.append((nx, ny))
    return currentVisited

def makeBoard():
    for j in range(6):
        for i in range(11, -1, -1):
            if board[i][j] == '.': 
                continue
            for k in range(11, i, -1):
                if board[k][j] == '.':
                    board[k][j] = board[i][j]
                    board[i][j] = '.'
    

board = [list(map(str, sys.stdin.readline().strip())) for _ in range(12)]
ans = 0
while True :
    isChanged = False
    for i in range(11, -1, -1):
        for j in range(6) :
            if board[i][j] != '.':
                tempArr = dfs(i, j)
                if len(tempArr) >= 4 :
                    if not isChanged :
                        isChanged = True
                    for x, y in tempArr :
                        board[x][y] = '.'
    makeBoard()
    if isChanged :
        ans += 1
    else :
        break
print(ans)