'''
풀이일자 : 2020/06/03
문제 이름 : 예산
문제 번호 : 2512
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 이분탐색(BinarySearch)
최대한으로 예산을 배정하는 방법
'''
import sys

def binarySearch(low, high) :
    ans = 0
    while low <= high :
        mid = (low + high) // 2
        sumBudget = 0
        for budget in budgets :
            sumBudget += min(budget, mid)
        if sumBudget <= m :
            ans = max(mid, ans)
            low = mid + 1
        else :
            high = mid - 1
    return ans

n = int(sys.stdin.readline().strip())
budgets = list(map(int, sys.stdin.readline().strip().split()))
budgets.sort()
m = int(sys.stdin.readline().strip())
if sum(budgets) < m:
    print(max(budgets))
    exit()
left = 0
right = max(budgets)
print(binarySearch(left, right))