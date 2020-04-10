# 풀이일자 : 2020/04/10
# 문제 이름 : 케빈 베이컨의 6단계 법칙
# 문제 번호 : 1389
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 케빈 베이컨의 수가 가장 작은 사람
# 플로이드 워셜로 해결할 수 있는 문제.
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
result = []
path = [[0] * n for i in range(n)]
for i in range(m):
    start, end = map(int, sys.stdin.readline().strip().split())
    path[start-1][end-1] = 1
    path[end-1][start-1] = 1

#플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n): 
            if path[i][j] > path[i][k] + path[k][j]:
                path[i][j] = path[i][k] + path[k][j]
for i in range(n):
    result.append(sum(path[i]))
print(result.index(min(result)) + 1)