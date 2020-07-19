'''
문제 이름 : 펠린드롬인지 확인하기
문제 번호 : 10988
풀이 일자 : 2020.07.20
'''
import sys

string = sys.stdin.readline().strip()
length = len(string)
if length % 2 == 0 :
    start = length // 2 - 1
    end = length // 2
else :
    start = length // 2 - 1
    end = length // 2 + 1
while start >= 0 or end < length :
    if string[start] != string[end]:
        print(0)
        sys.exit()
    start -= 1
    end += 1
print(1)
