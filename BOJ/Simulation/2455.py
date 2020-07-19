'''
문제 이름 : 지능형 기차
문제 번호 : 2455
풀이 일자 : 2020.07.19
'''
import sys

numOfStat = 4
maxAvailable = 10000

inputs = []
answer = 0
current = 0
for i in range(numOfStat):
    getOff, getIn = list(map(int, (sys.stdin.readline().strip().split())))
    current = current - getOff + getIn
    assert current <= maxAvailable
    answer = max(answer, current)
print(answer)
