'''
문제 이름 :N으로 표현
dp[i] : N을 i개 사용하여 구할 수 있는 숫자들
'''

def solution(N, number):
    
    dp = [0,[N]]
    if N == number:
        return 1
    for i in range(2, 9):
        temp = []
        basic_num = int(str(N) * i)
        temp.append(basic_num)
        for j in range(1, i//2+1):
            for x in dp[j]:
                for y in dp[i-j]:
                    temp.append(x+y)
                    temp.append(x-y)
                    temp.append(y-x)
                    temp.append(x*y)
                    if y !=0:
                        temp.append(x/y)
                    if x !=0:
                        temp.append(y/x)
            if number in temp:
                return i
            dp.append(temp)
    return -1