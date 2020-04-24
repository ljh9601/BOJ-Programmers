# 풀이일자 : 2020/04/24
# 문제 이름 : 사전
# 문제 번호 : 1256
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# k번째 사전에 수록되어있는 문자열
# dp의 정의 : dp[i][j]란 a를 i개, z를 j개 추가했을 때 나올 수 있는 문자열의 개수.
# 풀이 방식은 findStr 함수로 i, j를 줄여가며 i혹은 j가 0이 될 때까지 결과 string에 a와 z를 추가하면 된다.
import sys
import itertools

ans = ''

def findStr(nV, mV, kV):
    global ans
    if nV == 0 :
        for _ in range(mV) :
            ans += 'z'
        return
    if mV == 0 :
        for _ in range(nV) :
            ans += 'a'
        return
    if dp[nV-1][mV] >= kV :
        ans += 'a'
        findStr(nV-1, mV, kV)
    else :
        ans += 'z'
        findStr(nV, mV-1, kV - dp[nV-1][mV])
    return


n, m, k = map(int, sys.stdin.readline().strip().split())
dp = [[0] * (m+2) for _ in range(n+2)]
dp[1][1] = 2
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0 :
            dp[i][j] = 1
            continue
        nxtIVal = dp[i][j] * (i+j+1)//(i+1)
        nxtJVal = dp[i][j] * (i+j+1)//(j+1)
        dp[i+1][j] = nxtIVal if nxtIVal <= 1000000000 else 1000000001
        dp[i][j+1] = nxtJVal if nxtJVal <= 1000000000 else 1000000001
if dp[n][m] < k :
    print(-1)
    exit()
findStr(n, m, k)
print(ans)