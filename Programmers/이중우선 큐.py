'''
이중우선 큐
풀이일자 : 2020.06.10
'''

from collections import deque

def solution(operations):
    q = deque()
    for val in operations:
        val = val.split(" ")
        if val[0] == 'I':
            q.append(int(val[1]))
        elif val[0] == 'D' :
            if val[1] == '1' and q:
                q.remove(max(q))
            if val[1] == '-1'and q:
                q.remove(min(q))
    return [0,0] if not q else [max(q), min(q)]