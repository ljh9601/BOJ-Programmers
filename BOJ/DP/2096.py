# 풀이일자 : 2020/03/31
# 문제 이름 : 내려가기
# 문제 번호 : 2096
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : 다이나믹 프로그래밍 
# 얻을 수 있는 최대 및 최소 점수
# dp의 정의 : n번째 줄에서 0~2번째 인덱스를 택했을 때의 각각의 최대 및 최소 비용
import sys

n = int(sys.stdin.readline().strip())
inputs = [0] * 3
dpMax = [0] * 6
dpMin = [0] * 6

for i in range(0, n):
    inputs = list(map(int, sys.stdin.readline().strip().split()))
    dpMax[0] = max(dpMax[3], dpMax[4]) + inputs[0]
    dpMax[1] = max(dpMax[3], dpMax[4], dpMax[5]) + inputs[1]
    dpMax[2] = max(dpMax[4], dpMax[5]) + inputs[2]

    dpMin[0] = min(dpMin[3], dpMin[4]) + inputs[0]
    dpMin[1] = min(dpMin[3], dpMin[4], dpMin[5]) + inputs[1]
    dpMin[2] = min(dpMin[4], dpMin[5]) + inputs[2]
    
    #메모리 초과 해결을 위한 덮어쓰기(Sliding Window)
    for j in range(3):
        dpMax[j+3] = dpMax[j]
        dpMin[j+3] = dpMin[j]

print('{0} {1}'.format(max(dpMax), min(dpMin)))