'''
풀이일자 : 2020/05/13
문제 이름 : 양팔 저울
문제 번호 : 2629
작성자 : 이장행
문제 출처 : 백준 온라인 저지
알고리즘 분류 : 다이나믹 프로그래밍
각 구슬에 대한 무게 측정 확인 가능 여부
'''
import sys

sinkerNum = int(sys.stdin.readline().strip())
sinkers = list(map(int, sys.stdin.readline().strip().split()))
marbleNum = int(sys.stdin.readline().strip())
marbles = list(map(int, sys.stdin.readline().strip().split()))
visited = [False] * (sum(sinkers) + 1)
visited[0] = True
for item in sinkers :
    for idx, value in enumerate(visited[:]) :
        if value :
            if not visited[idx + item] :
                visited[idx + item] = True

for item in sinkers :
    for idx, value in enumerate(visited[:]) :
        if value :
            if idx - item >= 0 :
                if not visited[idx - item] :
                    visited[idx - item] = True

for val in marbles :
    if val > len(visited) - 1 :
        print('N', end=' ')
    else :
        if visited[val] :
            print('Y', end=' ')
        else :
            print('N', end=' ')

'''
추의 무게 : 1 -> 1
추의 무게 : 1, 4 -> 1, 3, 4, 5
추의 무게 : 3, 4 -> 1, 3, 4, 7
추의 무게 : 1, 10 -> 1, 9, 10, 11
추의 무게 : 4, 10 -> 4, 6, 10, 14
추의 무게 : 1, 4, 10 -> 1, 3, 4, 5, 6, 9, 10, 11, 14
'''