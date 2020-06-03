'''
풀이일자 : 2020/06/03
문제 이름 : 공유기 설치
문제 번호 : 2110
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
가장 인접한 두 공유기 사이의 최대 거리
'''
import sys

def binary_search(low, high):
    result = 0
    while low <= high :
        cnt = 1
        currentHouse = houses[0]
        mid = (low + high) // 2
        for i in range(1, n):
            if currentHouse + mid <= houses[i] :
                currentHouse = houses[i]
                cnt += 1
        if cnt >= c :
            result = mid
            low = mid + 1
        else :
            high = mid - 1
    return result
    
n, c = map(int, sys.stdin.readline().strip().split())
houses = []
for i in range(n):
    housePos = int(sys.stdin.readline().strip())
    houses.append(housePos)
houses.sort()
left = 1
right = houses[-1] - houses[0]
print(binary_search(left, right))