# 풀이일자 : 2020/04/04
# 문제 이름 : 기타리스트
# 문제 번호 : 1495
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 마지막 곡 볼륨의 최댓값
# dp의 정의 : i번째 곡까지 연주했을 때 가능한지 여부 (트리 형식으로 검사하며 나아가야 함). 원하는 답은 마지막 줄 1이 저장된 마지막 칸의 인덱스.
import sys

n, s, m = map(int, sys.stdin.readline().strip().split())
volumes = list(map(int, sys.stdin.readline().strip().split()))
dp = [[-1] * (m+1) for i in range(n+1)]
dp[0][s] = volumes[0]
for i in range(1, n+1):
    for j in range(0, m+1):
        if dp[i-1][j] == -1 :
            continue
        if j + volumes[i-1] <= m :
            dp[i][j + volumes[i-1]] = 1
        if j - volumes[i-1] >= 0 :
            dp[i][j - volumes[i-1]] = 1
ans = -1
for i in range(m, -1, -1):
    if dp[-1][i] == 1 :
        ans = i
        break
print(ans)