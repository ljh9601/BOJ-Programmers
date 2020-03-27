def solution(string):
    dp = []
    dp.append(0)

    for i in range(0, (len(string)//2)):
        start = 0
        end = i + 1
        count = 1
        resultStr = ''
        startStr = string[start:end]
        restStr = string[end:]
        while restStr:
            compStr = restStr[start:end]
            restStr = restStr[end:]     
            if startStr != compStr:
                if count == 1 :
                    resultStr += startStr
                else :
                    resultStr += (str(count) + startStr)
                startStr = compStr
                count = 1
            else:
                count += 1
                startStr = compStr
        if count == 1 :
            resultStr += startStr
        else :
            resultStr += (str(count) + startStr)
        print(resultStr)
        dp.append(len(resultStr))
    return min(dp[1:])

if __name__ == "__main__":
    n = str(input())
    if len(n) == 0:
        print(0)
    else:
        print(solution(n))
