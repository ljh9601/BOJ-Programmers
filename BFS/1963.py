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

def primeList():
    prime = []
    for i in range(1000, 10000):
        if isPrime(i) :
            prime.append(i)
    return prime

def bfs(start, end):
    q = deque()
    q.appendleft(start)
    visited = [0] * 10000
    visited[int(start)] = 1
    while q :
        current = q.popleft()
        if current == end :
            return visited[int(current)] - 1
        for i in range(4):
            for j in range(9):
                nStart = dx[j] % 10
                result = int(current) + nStart * pow(10, 3-i)
                if result // 1000 > 0 and result in primeNums and not visited[result] :
                    visited[result] = visited[int(current)] + 1
                    q.append(str(result))
    return -1

t = int(sys.stdin.readline().strip())
primeNums = primeList()
for i in range(t):
    aNum, bNum = map(str, sys.stdin.readline().strip().split())
    ans = bfs(aNum, bNum)
    print(ans if ans >= 0 else 'Impossible')