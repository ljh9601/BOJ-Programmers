'''
문제 이름 : 숫자야구
문제 번호 : 2503
풀이 일자 : 2020.07.20
'''
import sys

n = int(input())
infos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
lst = []
for i in range(100, 1000):
    strI = str(i)
    if '0' in strI or len(set(strI)) != len(strI):
        continue
    lst.append(i)
answer = 0
for i in lst:
    strI = str(i)
    for j in range(len(infos)):
        numSt = 0
        numB = 0
        infoNum = str(infos[j][0])
        infoSt = infos[j][1]
        infoB = infos[j][2]
        for k in range(3):
            if strI[k] == infoNum[k] :
                numSt += 1
            elif strI[k] in infoNum and infoNum[k] != strI[k]:
                numB += 1
        if numSt != infoSt or numB != infoB :
            break
    else :
        answer += 1
print(answer)