# 풀이일자 : 2020/04/29
# 문제 이름 : 펠린드롬 분할
# 문제 번호 : 1509
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# dp의 정의 : dp[i][j] : stiring에서 i번째에서 j번째까지의 최소 펠린드롬 분할 개수.
import sys

string = sys.stdin.readline().strip()
length = len(string)

dp = [sys.maxsize] * (length+1)
dp[0] = 0
pelindrom = [[0] * (length+1) for _ in range(length+1)]
for i in range(1, length+1):
    pelindrom[i][i] = 1
for i in range(1, length):
    if string[i-1] == string[i] :
        pelindrom[i][i+1] = 1
for i in range(2, length):
    for j in range(1, length-i+1):
        if string[j-1] == string[i+j-1] and pelindrom[j+1][i+j-1] :
            pelindrom[j][i+j] = 1
for i in range(1, length+1):
    dp[i] = min(dp[i], dp[i-1]+1)
    for j in range(i+1, length+1):
        if pelindrom[i][j] :
            dp[j] = min(dp[j], dp[i-1] + 1)
print(dp[length])