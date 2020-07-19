'''
문제 이름 : 상수
문제 번호 : 2908
풀이 일자 : 2020.07.19
'''
import sys

num1, num2 = sys.stdin.readline().split()
print(max(int(num1[::-1]), int(num2[::-1])))