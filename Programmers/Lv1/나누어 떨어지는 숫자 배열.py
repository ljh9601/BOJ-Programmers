def solution(arr, divisor):
    answer = []
    for i in arr :
        if not i % divisor :
            answer.append(i)
    return sorted(answer) if answer else [-1]