def solution(strings, n): 
    temp = sorted(strings)
    answer = sorted(temp,key = lambda x : x[n])
    return answer