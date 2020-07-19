'''
풀이일자 : 2020/06/03
문제 이름 : K번째 수
문제 번호 : 1300
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
B[k]
'''
import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

left = 0
right = n**2 - 1
while left <= right :
    mid = (left + right) // 2
    if mid == k : 
        print(((k // n) + 1) * ((k % n) + 1))
        exit()
    elif mid > k :
        right = mid - 1
    else :
        left = mid + 1