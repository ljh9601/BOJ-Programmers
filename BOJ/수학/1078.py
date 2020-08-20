'''
문제 이름 : 뒤집음
문제 번호 : 1078
풀이 일자 : 2020.08.11
'''
import sys

def makeNum(string):
    string = string[::-1]
    for i in range(len(string)):
        if string[i] != '0':
            break
    return string[i:]

def make(string):
    for i in range(len(string)):
        if string[i] != '0':
            break
    return string[i:]

D = int(sys.stdin.readline().strip())
if D % 9 != 0 :
    print(-1)
    sys.exit()

for i in range(D, pow(1000000, 2)+1):
    if str(i)[0] < str(i)[-1]:
        continue
    reversedStr = makeNum(str(i))
    if i - int(reversedStr) == D :
        print(i)
        break
