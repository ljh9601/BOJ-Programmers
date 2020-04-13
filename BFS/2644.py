# 풀이일자 : 2020/04/13
# 문제 이름 : 촌수 계산
# 문제 번호 : 2644.py
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : BFS
# 두 사람의 촌수 계산
import sys
n = int(sys.stdin.readline().strip())
a, b = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())
path = {}
for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    if x not in path :
        path[x] = set({})
    if y not in path :
        path[y] = set({})
    path[x].add(y)
    path[y].add(x)
print(path)
