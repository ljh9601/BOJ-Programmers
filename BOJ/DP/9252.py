# 풀이일자 : 2020/03/31
# 문제 이름 : LCS2
# 문제 번호 : 9252
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍 
# 두 문자열의 최장 길이 부분 수열
# dp의 정의 : dp[i][j] = dp[i-1][j-1] + 1 or dp[i][j] = max(dp[i-1][j], dp[i][j-1])를 통해 길이 증가 dp를 구한 다음 거슬러 올라오며 대각선 확인하며 문자열 가져오고 reverse
import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
dp = [[0] * 1001 for i in range (1001)]
dpStr = []
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):  
        if str1[i-1] == str2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

len1 = len(str1)
len2 = len(str2)
while(dp[len1][len2] > 0) :
	if(dp[len1][len2] == dp[len1][len2-1]) :
		len2 -= 1
	elif(dp[len1][len2] == dp[len1-1][len2]) : 
		len1 -= 1
	elif(dp[len1][len2] - 1 == dp[len1-1][len2-1]) :
		dpStr.append(str1[len1-1])
		len1 -= 1
		len2 -= 1

print(dp[len(str1)][len(str2)])
if dp[len(str1)][len(str2)] > 0 :
    dpStr.reverse()
    print(''.join(dpStr))