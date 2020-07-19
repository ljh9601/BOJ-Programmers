'''
풀이일자 : 2020/06/02
문제 이름 : 수 찾기
문제 번호 : 1920
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
수가 카드들 속에 존재하는지 여부
'''

import sys

def binary_search(left, right, find):
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == find :
            return 1
        elif arr[mid] > find:
            right = mid - 1
        else:
            left = mid + 1
    return 0

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

m = int(sys.stdin.readline().strip())
toFind = list(map(int, sys.stdin.readline().strip().split()))

low = 0
high = len(arr) - 1

for val in toFind :
    print(binary_search(low, high, val))