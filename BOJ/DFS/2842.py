'''
풀이일자 : 2020/05/14
문제 이름 : 집배원 한상덕
문제 번호 : 2842
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : DFS
가장 적은 피로도로 모든 집에 배달을 하는 피로도
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

def dfs(posX, posY, leftVal, rightVal) :
    stack = deque()
    stack.appendleft((posX, posY))
    visited = [[False] * n for _ in range(n)]
    visited[posX][posY] = True
    while stack :
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :      
                if leftVal <= tired[nx][ny] <= rightVal and not visited[nx][ny] :
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    for i, j in houses :
        if not visited[i][j] :
            return False
    return True

n = int(sys.stdin.readline().strip())
board = [[] * n for _ in range(n)]
houses = []
postOffice = (0, 0)
for i in range(n):
    board[i] = list(map(str, sys.stdin.readline().strip()))
    for j in range(n):
        if board[i][j] == 'P' or board[i][j] == 'K':
            houses.append((i, j))
tired = [[0] * n for _ in range(n)]
tempList = []
h = []
for i in range(n):
    tired[i] = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(n) :
        if (i, j) in houses :
            h.append(tired[i][j])
        tempList.append(tired[i][j])
left_max = min(h)
right_min = max(h)
left_min = min(tempList)
right_max = max(tempList)
left = []
right = []
for val in sorted(tempList) :
    if left_min <= val <= left_max :
        left.append(val)
    if right_min <= val <= right_max :
        right.append(val)
left_idx = 0
right_idx = 0
ans = sys.maxsize
while left_idx < len(left) and right_idx < len(right) :
    leftCanGo = False; rightCanGo = False
    if dfs(houses[0][0], houses[0][1], left[left_idx], right[right_idx]) : # 주어진 피로도 제한을 사용하여 도달하는 경우 left를 증가시켜 제한을 강화
        ans = min(ans, right[right_idx] - left[left_idx])
        left_idx += 1
        leftCanGo = True
    else : # 주어진 피로도 제한으로는 모든 집을 도달하지 못하는 경우
        if leftCanGo and rightCanGo : # left를 증가시킬 수 있고, right 역시 증가시키는 경우
            left_idx += 1; right_idx += 1
        else : # 
            right_idx += 1
            rightCanGo = True
print(ans)