import sys
from collections import deque

n = int(sys.stdin.readline().strip())
nums = []
ans = ""
nums = deque([int(sys.stdin.readline().strip()) for _ in range(n)])
flag = True
stack = []
lastVal = 0

def delete(a, stack):
    global ans
    while stack and a <= stack[-1] :
        ans += '-'
        stack.pop()

while nums :
    current = nums.popleft()
    if current in stack:
        delete(current, stack)
    # Push해야 하면
    else:
        if current < lastVal :
            flag = False
            break
        for i in range(lastVal + 1, current + 1):
            ans += '+'
            stack.append(i)
        lastVal = current # Stack에서 가장 큰 수
        delete(current, stack)
if flag :
    for v in ans :
        print(v)
else :
    print('NO')