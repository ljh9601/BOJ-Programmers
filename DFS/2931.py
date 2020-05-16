'''
풀이일자 : 2020/05/16
문제 이름 : 가스관
문제 번호 : 2931
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : DFS
해커가 지운 칸의 위치와 그 칸에 원래 있던 블럭
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

def canGo(curX, curY) :
    c = board[curX][curY]
    if c == 'M' or c == 'Z':
        return [0, 1, 2, 3]
    if c == '|' :
        return [0, 1]
    if c == '-' :
        return [2, 3]
    if c == '+' :
        return [0, 1, 2, 3]
    if c == '1' :
        if visited[curX][curY+1] > 0 :
            return [1]
        elif visited[curX+1][curY] > 0 :
            return [2]
    if c == '2' :
        if visited[curX-1][curY] > 0 :
            return [2]
        elif visited[curX][curY+1] > 0 :
            return [0]
    if c == '3' :
        if visited[curX][curY-1] > 0 :
            return [0]
        elif visited[curX-1][curY] > 0 :
            return [3]
    if c == '4' :
        if visited[curX][curY-1] > 0 :
            return [1]
        if visited[curX+1][curY] > 0 :
            return [3]

def dfs(start) :
    stack = deque()
    stack.append(start)
    visited[start[0]][start[1]] = True
    while stack :
        x, y = stack.pop()
        canGoList = canGo(x, y)
        print(x, y)
        for i in canGoList :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if board[x][y] == 'M' or board[x][y] == 'Z':
                    if board[nx][ny] in blocks :
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                else :
                    if board[nx][ny] in blocks :
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                    else :
                        if board[nx][ny] != 'M' and board[nx][ny] != 'Z' :
                            if (nx, ny) not in ansList:
                                ansList.append((nx, ny))
                            if (x-nx, y-ny) not in ansList :
                                ansList.append((x-nx, y-ny))
                                for k in range(4):
                                    tempX = nx + dx[k]
                                    tempY = ny + dy[k]
                                    if 0 <= tempX < r and 0 <= tempY < c :
                                        if not visited[tempX][tempY] and board[tempX][tempY] in blocks :
                                            visited[tempX][tempY] = True
                                            stack.append((tempX, tempY))
                                            #print(tempX, tempY)
    return False
def blockInsert(infoList) :
    global ret
    for info in infoList[1:] :
        if info == (0, 1) : #오른쪽으로 연결되어야 함
            ret += 1
        elif info == (0, -1) :# 왼쪽으로 연결되어야 함
            ret += 2
        elif info == (1, 0) : #아래로 연결되어야 함
            ret += 4
        elif info == (-1, 0) : #위로 연결되어야 함
            ret += 8

r, c = map(int, sys.stdin.readline().strip().split())
board = [['0'] * c for _ in range(r)]
blocks = ['|', '-', '+', '1', '2', '3', '4']
connectInfo = [12, 3, 15, 5, 9, 10, 6]
visited = [[False] * c for _ in range(r)]
ansList = []
ret = 0
for i in range(r):
    board[i] = list(map(str, sys.stdin.readline().strip()))
    for j in range(c):
        if board[i][j] == 'M' :
            start = (i, j)
        if board[i][j] == 'Z' :
            end = (i, j)
if not dfs(start) :
    dfs(end)
print(ansList)
blockInsert(ansList)
if ret not in connectInfo :
    for i in range(4):
        nx = ansList[0][0] + dx[i]
        ny = ansList[0][1] + dy[i]
        if 0 <= nx < r and 0 <= ny < c :
            if board[nx][ny] == 'M' or board[nx][ny] == 'Z' :
                ansList.append((dx[i], dy[i]))
    ret = 0
    blockInsert(ansList)
for i in range(r):
    print(visited[i])
print('{} {} {}'.format(ansList[0][0]+1, ansList[0][1]+1, blocks[connectInfo.index(ret)]))
