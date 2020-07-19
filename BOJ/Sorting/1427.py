'''
문제 이름 : 소트인사이드
문제 번호 : 1427
풀이 일자 : 2020.07.19
'''
import sys

num = int(sys.stdin.readline().strip())
print(int(''.join(sorted(list(str(num)), reverse = True))))