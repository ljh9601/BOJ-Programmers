'''
문제 이름 : 다이얼
문제 번호 : 5622
풀이 일자 : 2020.07.19
'''
import sys

inputs = sys.stdin.readline().strip()
dic = dict()
idx = 0
answer = 0
for i in range(2, 10):
    dic[i] = list()
for i in range(2, 10):
    if i == 7 or i == 9:
        for j in range(4):
            dic[i].append(chr(ord('A') + idx))
            idx += 1
        continue
    for j in range(3):
        dic[i].append(chr(ord('A') + idx))
        idx += 1
for v in inputs :
    for (key, value) in dic.items() :
        if v in value :
            answer += (key + 1)
print(answer)