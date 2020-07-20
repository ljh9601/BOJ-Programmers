'''
문제 이름 : 프린터 큐
문제 번호 : 1966
풀이 일자 : 2020.07.20
'''
import sys
from collections import deque

tcNum = int(sys.stdin.readline().strip())
answer = []
for _ in range(tcNum):
    n, m = map(int, sys.stdin.readline().strip().split())
    cnt = 0
    priority = list(map(int, sys.stdin.readline().strip().split()))
    queue = deque([[i, priority[i]] for i in range(n)])
    while queue :
        idx, val = queue.popleft()
        for i in range(len(queue)):
            if val < queue[i][1] :
                queue.append([idx, val])
                break
        else :
            if idx == m :
                answer.append(cnt+1)
                break
            else :
                cnt += 1
for ans in answer :
    print(ans)

    

