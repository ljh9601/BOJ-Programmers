'''
문제 이름 : 영화감독 숀
문제 번호 : 1436
풀이 일자 : 2020.08.11
'''
import sys

n = int(sys.stdin.readline().strip())
idx = 666
while n > 0 :
    if '666' in str(idx):
        n -= 1
        if not n :
            break
    idx += 1
print(idx)