def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    day = 0
    for i in range(a-1):
        day += months[i]
    day += b-1
    ans = (5 + day) % 7 
    return days[ans]