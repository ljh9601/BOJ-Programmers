def solution(s):
    answer = ""
    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            idx = 0
            continue
        if s[i].isalpha():
            if not idx % 2:
                answer += s[i].upper()
            else :
                answer += s[i].lower()
        else :
            answer += s[i]
        idx += 1
    return answer