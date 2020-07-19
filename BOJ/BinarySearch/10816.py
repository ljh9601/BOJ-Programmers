'''
풀이일자 : 2020/06/02
문제 이름 : 숫자 카드 2
문제 번호 : 10816
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지

lower bound와 upper bound를 사용한다!
-> lower bound : 찾고자(넣고자) 하는 원소가 나타나는 첫 위치
-> upper bound : 찾고자 하는 원소보다 큰 값이 나타나는 첫 위치
일반적인 이분탐색과 거의 다르지 않음

https://12bme.tistory.com/120 <- 아주 잘 설명되어있으니 참고

lower bound : low와 high의 구간 설정에서 오른쪽 끝을 포함하면서 와야 함
upper bound : low와 high의 구간 설정에서 왼쪽쪽 끝을 포함하면서 와야 함
'''
import sys

def lower_bound(low, high, val):
    while low < high :
        mid = (low + high) // 2
        if cards[mid] < val :
            low = mid + 1
        else :
            high = mid
    return high + 1

def upper_bound(low, high, val):
    while low < high :
        mid = (low + high) // 2
        if cards[mid] <= val :
            low = mid + 1
        else :
            high = mid
    return high + 1

n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
toFind = list(map(int, sys.stdin.readline().strip().split()))
cards.sort()
left = 0
right = len(cards)
for find in toFind :
    print(upper_bound(left, right, find) - lower_bound(left, right, find), end=' ')