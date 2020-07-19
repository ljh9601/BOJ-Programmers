import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

small = n - m

result = 1
div = 1
while n > small :
    result *= n
    n -= 1
while m > 0 :
    div *= m
    m -= 1
result = result // div
print(result % 10007)