def solution(n):
    arr = [i for i in range(n+1)]
    answer = 0
    for i in range(2, n+1):
        if arr[i] == 0 :
            continue
        for j in range(2*i, n+1, i):
            arr[j] = 0
    for val in arr[2:] :
        if val :
            answer += 1
    return answer