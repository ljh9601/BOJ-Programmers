'''
풀이일자 : 2020/06/03
문제 이름 : 나는야 포켓몬 마스터 이다솜
문제 번호 : 1620
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
포켓몬의 숫자, 숫자에 해당하는 포켓몬 이름
'''
import sys

def binary_search(low, high, val) :
    if 'A' <= val[0] <= 'Z' :
        while low <= high :
            mid = (low + high) // 2
            if sortedBook[mid][0] == val :
                return sortedBook[mid][1]
            elif sortedBook[mid][0] < val :
                low = mid + 1
            else :
                high = mid - 1
    else :
        return book[int(val)]

n, m = map(int, sys.stdin.readline().strip().split())
book = ['-1'] + [sys.stdin.readline().strip() for _ in range(n)]
toFind = [sys.stdin.readline().strip() for _ in range(m)]
sortedBook = []
left = 1
right = n
for a, b in enumerate (book):
    sortedBook.append([b, a])
sortedBook.sort()
for find in toFind :
    print(binary_search(left, right, find))