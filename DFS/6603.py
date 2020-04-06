# 풀이일자 : 2020/04/05
# 문제 이름 : 로또
# 문제 번호 : 6603
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS (하지만 DFS로 풀지 않았다..ㅋㅋ)
# 가능한 조합들
# python의 itertools 모듈을 이용하여 쉽게 Solve

import sys
from itertools import combinations

while True :
    inputs = list(map(int, sys.stdin.readline().strip().split()))
    k = inputs[0]
    if k == 0 :
        exit()
    del inputs[0]
    lst = list(combinations(inputs, 6))
    for i in lst :
        for j in i :
            print(j, end=' ')
        print()
    print()