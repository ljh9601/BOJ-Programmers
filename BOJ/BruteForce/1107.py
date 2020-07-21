'''
문제 이름 : 리모컨
문제 번호 : 1107
풀이 일자 : 2020.07.21
'''
import sys, math

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
available = []
if m > 0 :
    notWork = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(10):
        if i not in notWork :
            available.append(i)
else :
    for i in range(10):
        available.append(i)
smaller = ""
bigger = ""
answer = 0

if n == 100 :
    print(0)
    sys.exit()
if not available :
    print(abs(100 - n))
    sys.exit()
if available == [0]:
    if n == 0 :
        print(1)
        sys.exit()
    else :
        print(min(abs(n - 100), n+1))
        sys.exit()
# 만들 수 있는 다음 큰 숫자.
# 만들 수 있는 다음으로 작은 숫자를 만들어야 한다.
idx = 0
smallerCnt = 0
biggerCnt = 0
while True:
    flagBigger = True
    flagSmaller = True
    if bigger and smaller :
        break
    idx += 1
    if not bigger :
        for ch in str(n + idx) :
            if int(ch) not in available :
                flagBigger = False
                break
        if flagBigger:
            bigger = str(n+idx)
            biggerCnt += len(bigger)
    if n == 0 :
        smaller = '999999999'
    if n - idx >= 0 and not smaller:
        for ch in str(n - idx) :
            if int(ch) not in available :
                flagSmaller = False
                break
        if flagSmaller :
            smaller = str(n-idx)
            smallerCnt += len(smaller)
            
answer = min(abs(100 - n), smallerCnt + abs(int(smaller) - n), biggerCnt + abs(int(bigger) - n))
print(answer)