def solution(s, n):
    answer = ''
    for ch in s :
        if ch.isupper():
            if ord(ch) + n > ord('Z'):
                answer += chr((ord(ch)+n - ord('Z')))
        elif ch.islower() :
            if ord(ch) + n > ord('z'):
                answer += chr((ord(ch)+n - ord('z')))
        else :
            answer += ' '
    return answer