'''
문제 이름 : 방 번호
문제 번호 : 2941.py
풀이 일자 : 2020.07.20
'''
import sys

n = list(sys.stdin.readline().strip())
check = [1] * 10
answer = 1
for ch in n :
    if check[int(ch)] > 0:
        check[int(ch)] -= 1
    else :
        if ch == '6' and check[9]:
            check[9] -= 1
        elif ch == '9' and check[6] :
            check[6] -= 1
        else :
            answer += 1
            for i in range(10):
                if i == int(ch):
                    continue
                check[i] += 1
print(answer)
            


