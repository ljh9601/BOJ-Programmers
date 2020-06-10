'''
입국심사
풀이일자 : 2020.06.10
'''

def solution(n, times):
    left = 0
    right = max(times) * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2    
        pe = 0
        for val in times :
            pe += mid // val
        if pe >= n :
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer