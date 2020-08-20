'''
문제 이름 : 보물
문제 번호 : 1026
풀이 일자 : 2020.08.11
'''

import sys

n = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
sortedA = sorted(A)
sortedB = sorted(B)
ans = 0

for i in range(n):
    maxB = sortedB.pop(len(sortedB) - 1)
    #maxBIdx = B.index(maxB)
    minA = sortedA.pop(0)
    #minAIdx = A.index(minA)
    ans += minA * maxB
print(ans)
