# 풀이일자 : 2020/04/13
# 문제 이름 : 공통 부분 문자열
# 문제 번호 : 5582
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 가장 긴 공통 문자열의 길이
# DP의 정의 : 두 문자열을 비교하며 각각의 위치에서의 공통 부분 값을 dp 2차원 배열로 표현하고, 이 dp 배열의 최댓값이 답이 된다.
# 다만, Python3로 채점하면 시간 초과가 나니, 속도 면에서 크게 개선된 PyPy3로 채점해야 한다.
import sys
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
length1 = len(str1)
length2 = len(str2)
dp = [[0] * (length2+1) for i in range(length1+1)]
ans = 0
for i in range(1, length1+1) :
    for j in range(1, length2+1) :
        if str1[i - 1] == str2[j - 1] :
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
print(ans)