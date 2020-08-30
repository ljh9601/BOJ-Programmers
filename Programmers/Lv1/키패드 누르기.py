def solution(numbers, hand):
    answer = ''
    # 왼손, 오른손의 초기 좌표 설정
    leftPos = (3,0); rightPos = (3,2)
    for val in numbers :
        # 0인 경우 좌표처리를 위해 따로 예외처리
        if val == 0:
            val = 11
        # 눌러야 할 숫자의 좌표를 valPos에 저장
        valPos = ((val-1)//3, (val+2)%3)
        
        # 눌러야 할 숫자가 1,4,7 중에 하나라면 무조건 왼손
        if val in [1,4,7]:
            answer += 'L'
            leftPos = valPos
            continue
            
        # 눌러야 할 숫자가 3,6,9 중에 하나라면 무조건 오른손
        elif val in [3,6,9]:
            answer += 'R'
            rightPos = valPos
            continue
            
        # 거리의 대소 비교만 하면 되기 때문에 맨해튼 거리를 사용
        distLeft = abs(valPos[0] - leftPos[0]) + abs(valPos[1] - leftPos[1])
        distRight = abs(valPos[0] - rightPos[0]) + abs(valPos[1] - rightPos[1])
        
        # 왼손과 오른손 사이의 값이 같다면 오른손잡이라면 오른손, 왼손잡이라면 왼손 이동
        if distLeft == distRight :
            if hand == 'left':
                answer += 'L'
                leftPos = valPos
            else :
                answer += 'R'
                rightPos = valPos
        else :
            if distLeft < distRight :
                answer += 'L'
                leftPos = valPos
            else :
                answer += 'R'
                rightPos = valPos
    return answer