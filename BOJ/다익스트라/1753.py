# 우선순위큐의 정렬 기준은 Cost가 돼야 한다.

import sys, heapq  

def dijkstra(v, start, path, dist):
    heapq.heapify(heap)
    while heap :
        curCost, current = heapq.heappop(heap)
        if dist[current] < curCost :
            continue
        for st, cost in path[current]:
            cost += curCost
            if dist[st] > cost :
                dist[st] = cost
                heapq.heappush(heap, [cost, st])

v, e = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline().strip())
INF = sys.maxsize
path = [[] for _ in range(v+1)]
dist = [INF] * (v+1)
dist[start] = 0
heap = [[0, start]]

for _ in range(e):
    st, e, cost = map(int, sys.stdin.readline().strip().split())
    path[st].append([e, cost])
dijkstra(v, start, path, dist)
for i in range(1, v+1):
    print(dist[i] if dist[i] != INF else 'INF')