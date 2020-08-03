def solution(n):
    answer = ""
    for i in range(n):
        if not i % 2 :
            answer += "수"
        else :
            answer += "박"
    return answer