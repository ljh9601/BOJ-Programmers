'''
문제 이름 : 정렬
문제 번호 : 10989
풀이 일자 : 2020.08.11
'''
import sys

n = int(sys.stdin.readline().strip())
check = [0] * 10001
for i in range(n):
    check[int(sys.stdin.readline().strip())] += 1
for i in range(10001):
    if check[i] :
        for j in range(check[i]):
            print(i)