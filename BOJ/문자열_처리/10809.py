'''
문제 이름 : 알파벳 찾기
문제 번호 : 10809
풀이 일자 : 2020.07.19
'''
import sys

alphaNum = 26
inputs = sys.stdin.readline().strip()
answer = []
for i in range(alphaNum):
    answer.append(inputs.find(chr(ord('a') + i)))
for v in answer :
    print(v, end= ' ')