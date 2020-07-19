# 풀이일자 : 2020/05/02
# 문제 이름 : LCS 3
# 문제 번호 : 1958
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 세 문자열의 LCS
# DP의 정의 : dp[n][m][k]란 string1, string2, string3 까지의 각각 n번째, m번째, k번째까지에서 최대의 LCS 길이.
import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
str3 = sys.stdin.readline().strip()
len1 = len(str1)
len2 = len(str2)
len3 = len(str3)
dp = [[[0] * (len2+1) for i in range(len1+1)] for j in range(len3+1)]
temp = 0

for k in range(1, len3+1) :
    for i in range(1, len1+1) :
        for j in range(1, len2+1) :        
            if str3[k-1] == str1[i-1] == str2[j-1] :                
                dp[k][i][j] = dp[k-1][i-1][j-1] + 1
            else : 
                dp[k][i][j] = max(dp[k - 1][i][j], dp[k][i - 1][j], dp[k][i][j - 1], dp[k - 1][i - 1][j], dp[k][i - 1][j - 1], dp[k - 1][i][j - 1])
print(dp[k][i][j])

# dp[1][5][3] = 1
# dp[2][6][4] = 2
# dp[3][7][5] = 3