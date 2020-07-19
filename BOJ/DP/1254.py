'''
풀이일자 : 2020/05/14
문제 이름 : 펠린드롬 만들기
문제 번호 : 1254
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 다이나믹 프로그래밍
Manacher's Algorithm을 사용하면 DP를 사용하지 않고 간편하게 O(N)으로 풀이 가능!
'''
import sys

def pelindrom(idx) :
    i = 0
    while i + idx < length - i - 1 :
        if s[idx+i] != s[length-i-1] :
            return False
        i += 1
    return True

s = list(map(str, sys.stdin.readline().strip()))
ans = 0
length = len(s)
for i in range(0, length) :
    if pelindrom(i) :
        ans = i + length
        break
print(ans if ans > 0 else length * 2 - 1)