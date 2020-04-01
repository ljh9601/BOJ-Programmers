# 풀이일자 : 2020/04/01 (이전 풀이 문제 수정)
# 문제 이름 : 암호코드
# 문제 번호 : 2011
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍
# 암호의 해석 가짓수
# dp의 정의 : n번째 인덱스까지 나올 수 있는 암호의 가짓수
import sys

n = str(sys.stdin.readline().strip())
inputList = list(n)

if int(inputList[0]) == 0:
    print(0)
else:
    dp = []
    dp.append(1)
    for i in range (1, len(n)+1):
        temp = 0
        if i>=2 :
            temp = int(inputList[i-2] + inputList[i-1])
        if int(inputList[i-1]) == 0:
            dp.append(0)
        else:
            dp.append(dp[i-1])
        
        if temp >= 10 and temp < 27:
            dp[i] = (dp[i]+dp[i-2]) % 1000000
    result = dp[len(n)] % 1000000
    print(result)