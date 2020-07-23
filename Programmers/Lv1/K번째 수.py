'''
K번째 수
'''
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end, kth = commands[i]
        newArr = array[start-1:end]
        newArr.sort()
        answer.append(newArr[kth-1])
        
    return answer