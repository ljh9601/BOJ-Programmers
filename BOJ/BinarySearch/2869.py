'''
풀이일자 : 2020/06/02
문제 이름 : 달팽이는 올라가고 싶다.
문제 번호 : 2869
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
달팽이가 나무 막대를 모두 올라가는데 걸리는 시간
'''
import sys

a, b, v = map(int, sys.stdin.readline().strip().split())
k = (v-b) / (a-b)
print(int(k) if k == int(k) else int(k) + 1)