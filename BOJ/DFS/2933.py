'''
풀이일자 : 2020/05/12
문제 이름 : 미네랄
문제 번호 : 2933
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : DFS
모든 막대를 던지고 난 후의 미네랄 모양
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def destroy(floor, direction) :
    foundX = floor; foundY = 0
    if direction == 1 :
        for i in range(c-1, -1, -1) :
            if board[floor][i] == 'x' :
                board[floor][i] = '.'
                foundY = i
                break
    else :
        for i in range(c) :
            if board[floor][i] == 'x' :
                board[floor][i] = '.'
                foundY = i
                break
    for i in range(4):
        nx = foundX + dx[i]
        ny = foundY + dy[i]
        if 0 <= nx < r and 0 <= ny < c :
            if board[nx][ny] == 'x' :
                destroyQ.append((nx, ny))

def dfs(posX, posY) :
    stack = deque()
    visited = [[False] * c for _ in range(r)]
    fallList = []
    stack.append((posX, posY))
    visited[posX][posY] = True
    while stack:
        x, y = stack.pop()
        if x == r-1:
            return
        if board[x+1][y] == '.':
            fallList.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] == 'x' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    stack.append([nx, ny])

    fall(visited, fallList)

def fall(check, fall_list):
    k, flag = 1, 0
    while True:
        for i, j in fall_list:
            if i + k == r-1:
                flag = 1
                break
            if board[i+k+1][j] == 'x' and not check[i+k+1][j]:
                flag = 1
                break
        if flag:
            break
        k += 1

    for i in range(r-2, -1, -1):
        for j in range(c):
            if board[i][j] == 'x' and check[i][j]:
                board[i][j] = '.'
                board[i+k][j] = 'x'


r, c = map(int, sys.stdin.readline().strip().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
throwCnt = int(sys.stdin.readline().strip())
throws = list(map(int, sys.stdin.readline().strip().split()))
destroyQ = deque()
for pos in range(throwCnt) :
    relativePos = r - throws[pos]
    direction = 0 if pos % 2 == 0 else 1 # 왼쪽에서 던지는 경우 : 1, 오른쪽에서 던지는 경우 : 0
    destroy(relativePos, direction)
    while destroyQ :
        x, y = destroyQ.popleft()
        dfs(x, y)
for i in range(r):
    for j in range(c):
        print(board[i][j], end='')
    print('')