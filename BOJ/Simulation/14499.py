import sys

def move(direction, arr, current, n, m):
    if direction == 1 :
        if current[1] + 1 == m : 
            return False
        current = (current[0], current[1] + 1)    
    elif direction == 2 :
        if current[1]-1 < 0 :
            return False
        current = (current[0], current[1] - 1)
    elif direction == 3 :
        if current[0]-1 < 0 :
            return False
        current = (current[0] - 1, current[1])
    elif direction == 4 :
        if current[0]+1 == n :
            return False
        current = (current[0] + 1, current[1])
    return current

def reshape(current, arr, dice, direction, result):
    if direction == 1:
        temp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]    
        dice[3][1] = temp
        if arr[current[0]][current[1]] == 0 :
            arr[current[0]][current[1]] = dice[3][1]
        else :
            dice[3][1] = arr[current[0]][current[1]]
            arr[current[0]][current[1]] = 0
        result.append(dice[1][1])
        return
    if direction == 2:
        temp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]    
        dice[3][1] = temp
        if arr[current[0]][current[1]] == 0 :
            arr[current[0]][current[1]] = dice[3][1]
        else :
            dice[3][1] = arr[current[0]][current[1]]
            arr[current[0]][current[1]] = 0
        result.append(dice[1][1])
        return
    if direction == 3:
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp
        if arr[current[0]][current[1]] == 0 :
            arr[current[0]][current[1]] = dice[3][1]
        else :
            dice[3][1] = arr[current[0]][current[1]]
            arr[current[0]][current[1]] = 0
        result.append(dice[1][1])
        return
    if direction == 4:
        temp = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = temp
        if arr[current[0]][current[1]] == 0 :
            arr[current[0]][current[1]] = dice[3][1]
        else :
            dice[3][1] = arr[current[0]][current[1]]
            arr[current[0]][current[1]] = 0
        result.append(dice[1][1])
        return

if __name__ == "__main__":
    n, m, y, x, orderNum = list(map(int, sys.stdin.readline().strip().split()))

    arr = [[0] * m for i in range (n)]
    orders = []
    current = (y, x)
    result = []

    for i in range(0, n):
        inputs = list(map(int, sys.stdin.readline().strip().split()))
        for j in range (0, m):
            arr[i][j] = inputs[j]
    orders = list(map(int, sys.stdin.readline().strip().split()))
    dice = [[0] * 3 for i in range(4)]

    for i in range(0, orderNum):
        direction = orders[i]
        temp = move(direction, arr, current, n, m)
        if temp == False or temp == current:
            continue
        else :
            current = temp
            reshape(current, arr, dice, direction, result)
    for i in range(len(result) - 1) :
        print(result[i], end=' ')
    print(result[len(result) - 1])