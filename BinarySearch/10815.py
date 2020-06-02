'''
풀이일자 : 2020/06/02
문제 이름 : 숫자 카드
문제 번호 : 10815
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 여부
'''
import sys

def binary_search(low, high, val):
    while low <= high :
        mid = (low + high) // 2
        if cards[mid] == val :
            return 1
        elif cards[mid] > val :
            high = mid - 1
        else :
            low = mid + 1
    return 0

n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
toFind = list(map(int, sys.stdin.readline().strip().split()))
cards.sort()
left = 0
right = len(cards) - 1
for val in toFind :
    print(binary_search(left, right, val), end=' ')