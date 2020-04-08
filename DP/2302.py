# 풀이일자 : 2020/04/08
# 문제 이름 : 극장 좌석
# 문제 번호 : 2302
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DP
# 사람들이 좌석에 앉을 수 있는 가짓수
# DP의 정의 : VIP 석에 없다는 가정 하에 n번째 자리까지 사람들을 배치하는 경우의 수
import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
fixed = []
fixed.append(0)
for i in range(m):
    fixed.append(int(sys.stdin.readline().strip()))
fixed.append(n+1)

sub = []
for i in range(1, len(fixed)):
    sub.append(fixed[i] - fixed[i-1] - 1)

dp = []
dp.append(1)
dp.append(1)
dp.append(2)
dp.append(3)
for i in range(4, max(sub)+1):
    dp.append(dp[i-1] + dp[i-2])
ans = 1
for i in sub :
    ans *= dp[i]
print(ans)