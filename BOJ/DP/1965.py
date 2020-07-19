# 최대 길이의 증가하는 부분수열을 구하는 문제와 같음
# dp의 정의 : 수열에서 각 인덱스까지의 최대 증가하는 부분수열의 길이
import sys

n = int(input())
assert 1 <= n <= 1000
arr = list(map(int, sys.stdin.readline().strip().split()))
dp = []
dp.append(1)
for i in range(1, n):
    temp = []
    for j in range(0, i):
        if arr[i] > arr[j]:
            temp.append(dp[j])
    if not temp :
        dp.append(1)
    else :
        dp.append(max(temp) + 1)
print(max(dp))