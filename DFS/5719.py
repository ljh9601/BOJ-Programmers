# 풀이일자 : 2020/05/04
# 문제 이름 : 거의 최단 경로
# 문제 번호 : 5719
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 최단 경로 다음으로 짧은 최단 경로
# 다익스트라를 통해 최단 경로를 구한 후, BFS를 사용하여 백트래킹을 통한 경로를 저장해놓고, 다시 한번 다익스트라 알고리즘을 사용하며 최단 경로를 통하지 않는 최단 경로를 구하면 된다.
# 출처 : https://rebas.kr/701 님의 프로그래밍을 대부분 참고하였습니다. 문제가 된다면 지우겠습니다.

from collections import deque
from heapq import heappush, heappop
import sys


def dijkstra(a, dist, visited, depart):
    pq = []
    heappush(pq, (0, depart))
    for k in range(len(dist)):
        dist[k] = sys.maxsize
    dist[depart] = 0
    while pq:
        cost, now = heappop(pq)
        for nxt, ncost in a[now]:
            ncost += cost
            if dist[nxt] > ncost and not visited[now][nxt]:
                dist[nxt] = ncost
                heappush(pq, (ncost, nxt))


def bfs(b, dist, visited, depart, arrive):
    q = deque()
    q.append(arrive)
    while q:
        now = q.popleft()
        if now == depart:
            continue
        for prv, cost in b[now]:
            if dist[now] == dist[prv]+cost:
                visited[prv][now] = True
                q.append(prv)


while True:
    n, m = map(int, sys.stdin.readline().strip().split())
    if not n and not m:
        break
    s, d = map(int, sys.stdin.readline().strip().split())
    a = [[] for _ in range(n)]
    b = [[] for _ in range(n)]
    for i in range(m):
        u, v, p = map(int, sys.stdin.readline().strip().split())
        a[u-1].append([v-1, p])
        b[v-1].append([u-1, p])
    dist = [sys.maxsize] * n
    visited = [[False] * n for _ in range(n)]
    dijkstra(a, dist, visited, s-1)
    bfs(b, dist, visited, s-1, d-1)
    dijkstra(a, dist, visited, s-1)
    print(dist[d-1] if dist[d-1] != sys.maxsize else -1)