# 풀이일자 : 2020/04/16
# 문제 이름 : 반도체 설계
# 문제 번호 : 2352
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 연결선이 서로 꼬이지 않도록 하는 연결선의 최대 개수
# DP의 정의 : 최대 길이의 부분 증가수열을 구하면 된다.
# 하지만 n이 최대 40000이므로 O(n^2)으로 풀면 시간초과!
# 시간초과 Python3 Code
    # import sys
    # n = int(sys.stdin.readline().strip())
    # arr = list(map(int, sys.stdin.readline().strip().split()))
    # arr.insert(0, 0)
    # dp = [0] * (n+1)
    # dp[1] = 1
    # for i in range(2, n+1):
    #     temp = []
    #     for j in range(i):
    #         if arr[i] > arr[j] :
    #             temp.append(dp[j])
    #     if not temp :
    #         dp[i] = 1
    #     else :
    #         dp[i] = max(temp) + 1
    # print(max(dp))
# Lower bound를 이용한 O(n log n) Python3 Code (Index Tree를 이용해도 O(n log n)이 가능하다.)
import sys
from bisect import bisect_left
def solve():
    for i in arr[1:] :
        k = bisect_left(dp, i)
        if len(dp) <= k :
            dp.append(i)
        else :
            dp[k] = i
    return len(dp)

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.insert(0, 0)
dp = []
print(solve())