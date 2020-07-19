'''
문제 이름 : 그룹 단어 체커
문제 번호 : 1316.py
풀이 일자 : 2020.07.19
'''
import sys
n = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(n)]
answer = 0
for word in words :
    flag = True
    dic = dict()
    for v in word :
        dic[v] = list()
    for i in range(len(word)) :
        if dic[word[i]]:
            if dic[word[i]][-1] + 1 == i :
                dic[word[i]].append(i)
            else :
                flag = False
                break
        else :
            dic[word[i]].append(i)
    if flag :
        answer += 1
print(answer)