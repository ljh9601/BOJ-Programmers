def solution(s):
    s = s.lower()
    cntP = 0
    cntY = 0
    for c in s :
        if c == 'p':
            cntP += 1
        elif c == 'y':
            cntY += 1
    return True if cntP == cntY or (cntP==0 and cntY == 0) else False