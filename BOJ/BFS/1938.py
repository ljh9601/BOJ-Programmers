'''
풀이일자 : 2020/05/17
문제 이름 : 통나무 옮기기
문제 번호 : 1938
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : BFS
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0, 1, -1, 1, -1, 0]
dy = [0, 0, 1, -1, -1, 1, 1, -1, 0]
move = ['U', 'D', 'L', 'R', 'T']

def getMoveList(ch, flag) :
    if ch == 'U' or ch == 'D' or ch == 'L' or ch == 'R':
        return flag, [0, 1, 2, 3]
    if ch == 'T' :
        return not flag, [8]

def canRotate(nx, ny) :
    for i in range(8) :
        ndx = nx + dx[i]
        ndy = ny + dy[i]
        if 0 <= ndx < n and 0 <= ndy < n :
            if board[ndx][ndy] == '1' :
                return False
    return True

def bfs(start, end) :
    q = deque()
    q.appendleft(start)
    visited[start[0]][start[1]][start[2]] = 1
    while q :
        x, y, flag = q.popleft()
        if x == end[0] and y == end[1] and flag == end[2] :
            return visited[x][y][flag] - 1
        for toGo in move :
            nFlag, lst = getMoveList(toGo, flag)
            for i in lst :
                nx = x + dx[i]
                ny = y + dy[i]
                if toGo == 'T' : #회전의 경우 예외처리
                    if 0 < nx < n-1 and 0 < ny < n-1 :
                        if canRotate(nx, ny) and not visited[nx][ny][nFlag] :
                            visited[nx][ny][nFlag] = visited[x][y][flag] + 1
                            q.append((nx, ny, nFlag))
                else :
                    if flag : # 세워져있는 경우
                        if 0 < nx < n-1 and 0 <= ny < n :
                            if not visited[nx][ny][nFlag] :
                                if board[nx][ny] == '1' or board[nx-1][ny] == '1' or board[nx+1][ny] == '1' : #보드판 안에서 1이 있어 이동이 불가능한 경우
                                    continue
                                visited[nx][ny][nFlag] = visited[x][y][flag] + 1
                                q.append((nx, ny, nFlag))
                    else : # 누워져있는 경우
                        if 0 <= nx < n and 0 < ny < n-1 :
                            if not visited[nx][ny][nFlag] :
                                if board[nx][ny] == '1' or board[nx][ny+1] == '1' or board[nx][ny-1] == '1' : #보드판 안에서 1이 있어 이동이 불가능한 경우
                                    continue
                                visited[nx][ny][nFlag] = visited[x][y][flag] + 1
                                q.append((nx, ny, nFlag))
    return 0

n = int(sys.stdin.readline().strip())
board = [['0'] * n for _ in range(n)]
visited = [[[0] * 2 for _ in range(n)] for __ in range(n)]
init = []
last = []
for i in range(n) :
    board[i] = list(map(str, sys.stdin.readline().strip()))
    for j in range(n):
        if board[i][j] == 'B' :
            init.append((i, j)) # 항상 두번째 뽑힌 B가 Center임이 보증됨. 1 : 세워져있는 상태, 0 : 누워있는 상태
        if board[i][j] == 'E' :
            last.append((i, j))
start = [init[1][0], init[1][1], False]
end = [last[1][0], last[1][1], False]
if abs(init[1][0] - init[0][0]) == 1 : # 세워져있다면
    start[2] = True
if abs(last[1][0] - last[0][0]) == 1 : # 세워져있다면
    end[2] = True

print(bfs(start, end))