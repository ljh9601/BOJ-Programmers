'''
문제 이름 : 기하 알고리즘
문제 번호 : 3053
풀이 일자 : 2020.07.20
'''
import sys, math

n = int(sys.stdin.readline().strip())
circle = round(math.pow(n, 2) * math.pi, 6)
taxi = round((n * n) / 2 * 4, 6)
print(circle)
print(taxi)