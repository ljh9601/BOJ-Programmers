'''
문제 이름 : 알파벳 개수
문제 번호 : 10808.py
풀이 일자 : 2020.07.20
'''
import sys

inputs = sys.stdin.readline().strip()
answer = []
for i in range(26) :
    cnt = inputs.count(chr(ord('a') + i))
    answer.append(str(cnt))
print(' '.join(answer))