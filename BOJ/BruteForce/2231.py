'''
문제 이름 : 분해합
문제 번호 : 2309
풀이 일자 : 2020.07.20
'''
import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    strI = str(i)
    sums = i + sum([int(v) for v in strI])
    if sums == n :
        print(i)
        sys.exit()
print(0)
    