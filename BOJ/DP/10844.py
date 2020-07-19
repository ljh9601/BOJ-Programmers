n = int(input())

stair = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    temp = stair[:]
    stair[0] = temp[1]
    for j in range(1, 9) :
        stair[j] = (temp[j-1] + temp[j+1])
    stair[9] = temp[8]
    
print(sum(stair) % 1000000000)