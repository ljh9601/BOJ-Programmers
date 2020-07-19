'''
문제 이름 : 단어 공부
문제 번호 : 1157
풀이 일자 : 2020.07.19
'''
import sys

alphaNum = 26

inputs = sys.stdin.readline().strip().lower()
inputs = sorted(inputs)
alpha = dict()
for i in range(alphaNum):
    alpha.update({chr(ord('a') + i) : 0})
while inputs :
    alpha[inputs.pop()] += 1
res = sorted(alpha.items(), key = lambda x : -x[1])
if res[0][1] == res[1][1] :
    print('?')
else :
    print(res[0][0].upper())