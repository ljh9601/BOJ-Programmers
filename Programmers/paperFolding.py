def solution(n):
    dp = [''] * (n+1)
    dp[1] = '0'
    for i in range(2, n+1):
        dp[i] = dp[i-1] + '0' + dp[i-1]
        tempList = list(dp[i])
        tempList[2**i - (2**(i-2)+1)] = '0' if tempList[2**i - (2**(i-2)+1)] == '1' else '1'
        dp[i] = ''.join(tempList)
    return list(list(map(int, dp[n])))