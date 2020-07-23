def solution(arr):
    answer = [-1]
    for i in arr :
        if i != answer[-1] :
            answer.append(i)
    answer.pop(0)
    return answer