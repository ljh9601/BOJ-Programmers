'''
문제 이름 : 부분수열의 합
문제 번호 : 1966
풀이 일자 : 2020.07.20
'''
import sys, math
from itertools import combinations

n, s = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
answer = 0
for i in range(1, n+1):
    lst = list(combinations(numbers, i))
    for v in lst :
        if sum(v) == s :
            answer += 1
print(answer)