'''
풀이일자 : 2020/06/02
문제 이름 : 나무 자르기
문제 번호 : 2869
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
'''
import sys

def binary_search(left, high):
    while left <= high :
        ret = 0
        mid = (left + high) // 2
        for tree in trees :
            if tree > mid :
                ret += (tree - mid)
        if ret < m :
            high = mid - 1
        else :
            left = mid + 1
    return high

n, m = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))
trees.sort()
maxTree = max(trees)
print(binary_search(1, maxTree))