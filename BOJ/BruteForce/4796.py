import sys

idx = 1
while True :
    L, P, V = map(int, sys.stdin.readline().strip().split())
    if L == P == V == 0 :
        break
    div, mod = divmod(V, P)
    mod = min(mod, L)
    ans = div * L + mod
    print('Case {}: {}'.format(idx, ans))
    idx += 1