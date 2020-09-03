'''
풀이중....
'''

import sys

tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    posX = []
    posY = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        posX.append(x)
        posY.append(y)
    if n == 1 :
        print(1, 4)
        sys.exit()
    if n == 2 :
        if abs(posX[0] - posX[1]) == 1 and posY[0] == posY[1]:
            print(4, 6)
            sys.exit()
    if len(set(posX)) == 1 :
        for j in range(min(posY), max(posY)):
            if j + 1 not in posY :
                break
        else :
            print(, len(posY) * 2 + 2)
            sys.exit()
    resX, resY = 0, 0
    flag = False
    sortedX = sorted(posX)
    sortedY = sorted(posY)
    dist = 0
    cnt = 0
    if len(sortedX) % 2 == 0 :
        flag = True
        middleX1 = sortedX[(len(sortedX) // 2) - 1]
        middleX2 = sortedX[len(sortedX) // 2]
        resX = abs(middleX1 - middleX2) + 1
    else :
        middleX1 = sortedX[len(sortedX) // 2]
        middleX2 = middleX1
        resX = 1
    
    if len(sortedY) % 2 == 0 :
        flag = True
        middleY1 = sortedY[(len(sortedY) // 2) - 1]
        middleY2 = sortedY[len(sortedY) // 2]
        resY = abs(middleY1 - middleY2) + 1
    else :
        middleY1 = sortedY[len(sortedY) // 2]
        middleY2 = middleY1
        resY = 1
    if len(sortedX) % 2 == 0 and len(sortedY) % 2 == 0 :
        for x, y in zip(posX, posY):
            if min(middleX1, middleX2) <= x <= max(middleX1, middleX2) and min(middleY1, middleY2) <= y <= max(middleY1, middleY2):
                cnt += 1
    
    for x, y in zip(posX, posY):
        dist += (abs(x - middleX1) + abs(y - middleY1))
    print(dist, resX * resY - cnt)
'''
o o o o o
o o o o o
x o x o o
o o o o o
o o o x o
o o o o o
o o o x o
'''