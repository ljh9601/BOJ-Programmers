'''
모의고사
'''

#1번 : 1 2 3 4 5 반복
#2번 : (2,1) (2,3), (2,4), (2,5) 반복 
#3번 : 3,1,2,4,5 순서대로 각각 2번씩 반복

def solution(answers):
    answer = []
    answer.append([0, 1])
    answer.append([0, 2])
    answer.append([0, 3])
    personTwo = [2, 1, 2, 3, 2, 4, 2, 5]
    personThree = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if (i % 5) + 1 == answers[i] :
            answer[0][0] += 1
        if answers[i] == personTwo[i%8] :
            answer[1][0] += 1
        if answers[i] == personThree[i%10] :
            answer[2][0] += 1
    maxPerson = max(answer[0][0], answer[1][0], answer[2][0])
    result = []
    for i in range (0, len(answer)) :
        if maxPerson == answer[i][0] :
            result.append(answer[i][1])
    return sorted(result)