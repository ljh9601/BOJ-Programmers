'''
문제 이름 : 크로아티아 알파벳
문제 번호 : 2941.py
풀이 일자 : 2020.07.19
'''
import sys

croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
startCroatia = ['c', 'd', 'l', 'n', 's', 'z']
used = []
inputs = sys.stdin.readline().strip()
for v in croatia_alpha:
    if v in inputs :
        inputs = inputs.replace(v, ';')
print(len(inputs))

