'''
체육복
'''

def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for current in reserve_set:
        if current - 1 in lost_set :
            lost_set.remove(current-1)
        elif current + 1 in lost_set :
            lost_set.remove(current+1)
            
    return n - len(lost_set)