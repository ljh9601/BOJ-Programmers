import sys
from collections import deque

n = int(sys.stdin.readline().strip())
infos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
schedule = [0] * (1001)
infos = deque(sorted([[m, n] for n, m in infos], key = lambda x : (-x[0], x[1])))
while infos:
    point,leftDay = infos.popleft()
    if not schedule[leftDay] :
        schedule[leftDay] = point
    else :
        while schedule[leftDay] and leftDay > 0:
            leftDay -= 1
        if leftDay == 0 :
            continue
        schedule[leftDay] = point

print(sum(schedule))