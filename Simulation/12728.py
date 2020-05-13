import sys
import math

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    num = 3 + math.sqrt(5)
    ans = 0
    result = int(pow(num, n)) % 1000
    temp = str(result)
    listResult = list(temp)
    if len(listResult) < 3 :
        while len(listResult) < 3 :
            listResult.insert(0, 0)
    print('Case #' + str(_+1) + ': ', end = '')
    for i in listResult :
        print(i, end='')
    print('')