# 풀이일자 : 2020/04/03
# 문제 이름 : 줄세우기
# 문제 번호 : 2631
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 옮겨지는 아이의 최소의 수
# dp의 정의 : 가장 긴 증가하는 부분 수열의 길이를 구한 다음, 전체 수열의 길이에서 빼주면 이동시켜야 할 개수가 나옴.
import sys

n = int(sys.stdin.readline().strip())
arr = [0] * n
dp = []
dp.append(1)
count = 0
for i in range(n):
    arr[i] = int(sys.stdin.readline().strip())

for i in range(1, n):
    temp = []
    for j in range(0, i):
        if arr[i] > arr[j]:
            temp.append(dp[j])
    if not temp :
        dp.append(1)
        continue
    else :
        dp.append(max(temp) + 1)
print(n - max(dp))