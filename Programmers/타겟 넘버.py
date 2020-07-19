import sys
from collections import deque

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

if __name__ == "__main__" :
    numbers = list(map(int, sys.stdin.readline().strip().split()))        
    target = int(sys.stdin.readline())
    print(solution(numbers, target))