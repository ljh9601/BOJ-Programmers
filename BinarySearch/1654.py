'''
풀이일자 : 2020/06/02
문제 이름 : 랜선 자르기
문제 번호 : 1654
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
만들 수 있는 최대 랜선의 길이
'''
import sys

def binary_search(low, high):
    ans = 0
    while low <= high :
        cnt = 0
        mid = (low + high) // 2
        for val in lines :
            cnt += (val // mid)
        if cnt >= n :
            ans = mid
            low = mid + 1
        else :
            high = mid - 1
    return ans

k, n = map(int, sys.stdin.readline().strip().split())
lines = []
for i in range(k):
    lines.append(int(sys.stdin.readline().strip()))
left = 1
right = max(lines)
print(binary_search(left, right))