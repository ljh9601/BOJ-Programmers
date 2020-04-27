# 풀이일자 : 2020/04/24
# 문제 이름 : 소수 경로
# 문제 번호 : 1963
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 두 소수 사이의 필요한 최소 변환 횟수
# 
import sys
from collections import deque

dx = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def isPrime(num):
    for i in range(2, num):
        if num % i == 0 :
            return False
    return True

def bfs(start, end):
    q = deque()
    q.appendleft(start)
    visited[int(start)] = 1
    while q :
        current = int(q.popleft())
        if current == int(end) :
            return visited[current] - 1
        for i in range(10):
            if i != 0:
                nx = (current % 1000) + i * 1000
                if nx < 10000 and isPrime(nx) and not visited[nx]:
                    visited[nx] = visited[current] + 1
                    q.append(nx)
            nx = int(current / 1000) * 1000 + (current % 100) + i * 100
            if nx < 10000 and isPrime(nx) and  not visited[nx]:
                visited[nx] = visited[current] + 1
                q.append(nx)
            nx = int(current/100)*100 + (current % 10) + i * 10
            if nx < 10000 and isPrime(nx) and  not visited[nx]:
                visited[nx] = visited[current] +1
                q.append(nx)
            nx = int(current / 10) * 10 + i
            if nx < 10000 and isPrime(nx) and not visited[nx]:
                visited[nx] = visited[current] + 1
                q.append(nx)
    return -1

t = int(sys.stdin.readline().strip())
for i in range(t):
    aNum, bNum = map(str, sys.stdin.readline().strip().split())
    visited = [0] * 10000
    ans = bfs(aNum, bNum)
    print(ans if ans >= 0 else 'Impossible')