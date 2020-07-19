'''
문제 이름 : 단어의 개수
문제 번호 : 1152
풀이 일자 : 2020.07.19
'''
import sys
inputs = sys.stdin.readline().strip()
if inputs == '':
    print(0)
    sys.exit()
print(len(inputs.split(' ')))