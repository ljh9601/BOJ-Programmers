n = str(input())

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
            dp[i] = (dp[i]+dp[i-2])%1000000
    result = dp[len(n)]
    print(result)