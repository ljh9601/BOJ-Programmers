def solution(n):
    return int(''.join([v for v in sorted(str(n), reverse=True)]))