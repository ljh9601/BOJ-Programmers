'''
문제 이름 : 곱셈
문제 번호 : 1629
풀이 일자 : 2020.08.11
'''
import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

def cal(x, y, c):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 > 0:
        return cal(x, y-1, c) * x
    temp = cal(x, y // 2, c)
    temp %= c
    return temp**2 % c

print(cal(a, b, c) % c)
