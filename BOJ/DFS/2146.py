# 풀이일자 : 2020/04/16
# 문제 이름 : 다리 만들기
# 문제 번호 : 2146
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 두 대륙을 연결하는 가장 짧은 다리의 길이
# 문제 분류상 DFS로 나와있지만 다리 길이의 '최솟값'을 구하는 문제이므로 BFS로 Solve!
# 1단계 : 각각의 육지를 그룹화하며 바다를 oceans 큐에 집어넣음.
# 2단계 : oceans 큐 전체에서 BFS를 돌리며 육지의 크기 증가.
# 3단계 : BFS를 돌며 0이 아닌 이동할 칸을 만난 순간 다리 길이의 최소가 결정.
# 4단계 : oceans 큐를 한번씩 돌때마다 count를 증가시키며 이 count로 3단계의 종료 조건에서 답을 계산해줌.
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def groupLand(posX, posY, landNum) :
    q = deque()
    q.appendleft((posX, posY))
    board[posX][posY] = landNum
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if board[nx][ny] == 1:
                    board[nx][ny] = landNum
                    q.append((nx, ny))
                elif board[nx][ny] == 0 and (x, y) not in oceans:
                    oceans.append((x,y))
    return oceans

def bfs() :
    ans = sys.maxsize
    count = 0
    while oceans :
        count += 1
        length = len(oceans)
        for _ in range(length) :
            xO, yO = oceans.popleft()
            for i in range(4) :
                nxO = xO + dx[i]
                nyO = yO + dy[i]
                if 0 <= nxO < n and 0 <= nyO < n :
                    if board[nxO][nyO] == 0 :
                        board[nxO][nyO] = board[xO][yO]
                        oceans.append((nxO, nyO))
                    elif board[nxO][nyO] < board[xO][yO] :
                        ans = min(ans, (count - 1) * 2)
                    elif board[nxO][nyO] > board[xO][yO] :
                        ans = min(ans, count*2 - 1)
    return ans
n = int(sys.stdin.readline().strip())
board = [[0] * n for i in range(n)]
oceans = deque()
for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().strip().split()))
landNum = -1
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            groupLand(i, j, landNum)
            landNum -= 1
print(bfs())