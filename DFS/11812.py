'''
풀이일자 : 2020/05/18
문제 이름 : K진 트리
문제 번호 : 11812
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : DFS
DFS로 풀지 않고, 완전 K진 트리기 때문에 (N-2)/K + 1 공식을 이용하여 쉽게 풀이 가능!
'''
import sys

n, k, q = map(int, sys.stdin.readline().strip().split())
ans = []
for i in range(q) :
    x, y = map(int, sys.stdin.readline().strip().split())
    if k == 1 :
        print(abs(x-y))
        continue
    cnt = 0
    while x != y :
        maxVal = max(x, y)
        y = min(x, y)
        x = (maxVal-2)//k + 1
        cnt += 1
    ans.append(cnt)
for val in ans :
    print(val)