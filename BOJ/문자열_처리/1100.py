'''
문제 이름 : 하얀 칸
문제 번호 : 1100.py
풀이 일자 : 2020.07.20
'''
import sys

board = []
answer = 0

for i in range(8):
    board.append(sys.stdin.readline().strip())
    if i % 2 == 0 :
        for j in range(8):
            if j % 2 == 0 and board[i][j] == 'F':
                answer += 1
    else :
        for j in range(8):
            if j % 2 == 1 and board[i][j] == 'F':
                answer += 1
print(answer)    