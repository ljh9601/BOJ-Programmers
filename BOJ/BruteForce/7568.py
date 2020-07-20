'''
문제 이름 : 덩치
문제 번호 : 7568
풀이 일자 : 2020.07.20
'''
N = int(input())

people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for c in people :
    rank = 1 
    for n in people:
        if c == n :
            continue
        if (c[0]<n[0]) and (c[1]<n[1]): #3 w, h 모두 큰 경우
            rank += 1
    print(rank, end = ' ')