'''
풀이일자 : 2020/05/20
문제 이름 : 로고
문제 번호 : 9328
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : BFS, DFS
N개의 직사각형을 그리는데 필요한 PU 명령의 최솟값
Union Find 알고리즘을 사용해 각 직사각형의 개수를 구하면 됨.
'''

'''
FD x: 거북이를 x만큼 앞으로 전진
LT a: 거북이를 반시계 방향으로 a도 만큼 회전
RT a: 거북이를 시계 방향으로 a도 만큼 회전
PU: 연필을 올린다
PD: 연필을 내린다.
'''
import sys

def unionFind (root1, root2) :
    while root1 != rectangles[root1] :
        root1 = rectangles[root1]
    while root2 != rectangles[root2] :
        root2 = rectangles[root2]
    if root1 == root2 :
        return
    else :
        rectangles[root2] = root1

n = int(sys.stdin.readline().strip())
pos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
rectangles = [0] * 1001
rectanNo = 0
ans = 0
visited = {}
for startX, startY, endX, endY in pos:
    rectanNo += 1
    rectangles[rectanNo] = rectanNo
    for i in range(startX, endX+1) :
        if visited.get((i, startY)) :
            unionFind(rectanNo, visited[(i, startY)])
        if visited.get((i, endY)) :
            unionFind(rectanNo, visited[(i, endY)])
        visited[(i, startY)] = rectanNo
        visited[(i, endY)] = rectanNo
    for j in range(startY+1, endY+1) :
        if visited.get((startX, j)) :
            unionFind(rectanNo, visited[(startX, j)])
        if visited.get((endX, j)) :
            unionFind(rectanNo, visited[(endX, j)])
        visited[(startX, j)] = rectanNo
        visited[(endX, j)] = rectanNo
for i in range(1, 1001):
    if i == rectangles[i] :
        ans += 1

if visited.get((0, 0)): #0,0을 다시 방문했다면 -1 
    ans -= 1 if ans > 0 else 0 
print(ans)