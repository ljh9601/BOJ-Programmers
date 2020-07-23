def solution(s):
    length = len(s)
    ans = ""
    if length % 2 == 0 :
        ans += s[length // 2 - 1] + s[length // 2]
    else :
        ans = s[length // 2]
    return ans