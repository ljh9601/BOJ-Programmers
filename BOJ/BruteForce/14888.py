'''
문제 이름 : 선분 그룹
문제 번호 : 2309
풀이 일자 : 2020.07.20
'''
import sys

answer = []

def cal(n, numbers, plusCnt, minusCnt, mulCnt, divCnt, cnt):
    if cnt == len(numbers):
        answer.append(n)
        return
    curNum = numbers[cnt]
    if plusCnt > 0 :
        cal(n + curNum, numbers, plusCnt - 1, minusCnt, mulCnt, divCnt, cnt+1)
    if minusCnt > 0 :
        cal(n - curNum, numbers, plusCnt, minusCnt - 1, mulCnt, divCnt, cnt+1)
    if mulCnt > 0 :
        cal(n * curNum, numbers, plusCnt, minusCnt, mulCnt - 1, divCnt, cnt+1)
    if divCnt > 0 :
        res = n // curNum
        if n < 0 and curNum > 0 :
            n *= (-1)
            res = (n // curNum) * (-1)
        cal(res, numbers, plusCnt, minusCnt, mulCnt, divCnt - 1, cnt+1)
    

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
ops = list(map(int, sys.stdin.readline().strip().split()))
firstNum = numbers[0]
plusCnt, minusCnt, mulCnt, divCnt = (v for v in ops)
cal(firstNum, numbers, plusCnt, minusCnt, mulCnt, divCnt, 1)
print(max(answer))
print(min(answer))