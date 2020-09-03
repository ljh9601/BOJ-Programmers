def solution(x):
    return not x % sum([int(v) for v in str(x)])