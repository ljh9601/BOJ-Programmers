# 풀이일자 : 2020/05/02
# 문제 이름 : 역사
# 문제 번호 : 1613
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 사건의 전후 관계
# 플로이드 워셜로 해결할 수 있는 문제.

import sys

n, m = map(int, sys.stdin.readline().strip().split())
floyd = [[0] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    floyd[a-1][b-1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if floyd[i][k] and floyd[k][j] :
                floyd[i][j] = 1 #여기서는 경로 개수를 세줄 필요가 없으므로 True False 처럼 사용했다.
                #min(floyd[i][j], floyd[i][k] + floyd[k][j])
s = int(sys.stdin.readline().strip())
for j in range(s):
    qA, qB = map(int, sys.stdin.readline().strip().split())
    if floyd[qA-1][qB-1]:
        print(-1)
    elif floyd[qB-1][qA-1] :
        print(1)
    elif not floyd[qA-1][qB-1] :
        print(0)