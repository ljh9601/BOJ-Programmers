'''
문제 이름 : 명령 프롬프트
문제 번호 : 1032.py
풀이 일자 : 2020.07.20
'''
import sys

words, answer = [sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline().strip()))], ""
if len(words) == 1:
    print(words[0])
    sys.exit()
for i in range(len(words[0])):
    flag = True
    for j in range(1, len(words)):
        if words[j][i] != words[j-1][i] :
            flag = False
            break
    answer += words[j][i] if flag else '?'
print(answer)