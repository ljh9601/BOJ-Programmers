# 풀이일자 : 2020/04/22
# 문제 이름 : DSLR
# 문제 번호 : 9019
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# A에서 B로 변환하기 위한 최소한의 명령어 나열
# dx 배열을 D,S,L,R의 조합으로 짜고, 각각의 값 계산을 통해 BFS로 진행.
# BFS는 항상 최소 길이를 보장하기 때문에 탐색하며 명령어를 저장한다.
import sys
from collections import deque

dx = ['D', 'S', 'L', 'R']

def move(command, num):
    if command == 'D':
        ret = (num * 2) % 10000
        return ret
    if command == 'S':
        if num == 0 :
            return 9999
        else :
            return num - 1
    if command == 'L':
        return (num * 10 + num // 1000) % 10000
    if command == 'R':        
        return (num + (num%10) * 10000) // 10
    return 0

def bfs(start):
    q = deque()
    q.appendleft(start)
    visited[start] = ''
    while q :
        current = q.popleft()
        if current == int(b) :
            return visited[current]
        for i in range(4):
            nchr = move(dx[i], current)
            if 0 <= nchr < 10000 and visited[nchr] == '-1' :
                visited[nchr] = visited[current] + dx[i]
                q.append(nchr)

tcNum = int(sys.stdin.readline().strip())
result = [] * (tcNum)
for i in range(tcNum):
    a, b = map(str, sys.stdin.readline().strip().split())
    visited = ['-1'] * 10000
    result.append(bfs(int(a)))
for i in result :
    print(i)