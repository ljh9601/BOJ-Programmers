'''
풀이일자 : 2020/05/25
문제 이름 : 자동차 공장
문제 번호 : 2820
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : DFS
해당하는 직원의 월급 출력
세그먼트 트리와 propagation을 이용하여 O(log N)으로 풀어야 한다.
향후 과제로 남겨둠.
'''
import sys
from collections import deque

def dfs(start, salary) :
    stack = deque()
    stack.append(start)
    visited = [False] * (n+1)
    visited[start] = True
    while stack :
        current = stack.pop()
        for _, junior in enumerate(path[current]) :
            if not visited[junior] :
                visited[junior] = True
                stack.append(junior)
                sal[junior] += salary

n, m = map(int, sys.stdin.readline().strip().split())
path = {}
path[0] = set([])
path[1] = set([])
sal = [0] * (n+1)
salary = int(sys.stdin.readline().strip())
supervisor = 1
sal[1] = salary
for i in range(2, n+1):
    salary, supervisor = map(int, sys.stdin.readline().strip().split())
    if supervisor not in path :
        path[supervisor] = set([])
    if i not in path :
        path[i] = set([])
    path[supervisor].add(i)
    sal[i] = salary
for i in range(1, m+1):
    inputs = list(map(str, sys.stdin.readline().strip().split()))
    if inputs[0] == 'p' :
        dfs(int(inputs[1]), int(inputs[2]))
    elif inputs[0] == 'u' :
        print(sal[int(inputs[1])])