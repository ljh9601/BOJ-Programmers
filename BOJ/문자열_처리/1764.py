'''
문제 이름 : 듣보잡
문제 번호 : 1764
풀이 일자 : 2020.07.20
'''
import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().strip().split())
names = sorted(set([sys.stdin.readline().strip() for _ in range(n)]))
secNames = sorted(set([sys.stdin.readline().strip() for _ in range(m)]))
answer = []
cnt = Counter(names+secNames)
cnt = sorted(cnt.items(), key = lambda x : (-x[1], x[0]))

for (name, count) in cnt :
    if count > 1 :
        answer.append(name)
print(len(answer))
for v in answer :
    print(v)