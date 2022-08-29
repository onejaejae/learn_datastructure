# 나의 풀이법
def solution(a, b):
    month = {1:30, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = {2: "SUN", 3:"MON", 4:"TUE", 5: "WED", 6: "THU", 0: "FRI", 1: "SAT"}
    
    res = a-1
    sum = 0
    for i in range(1, res+1):
        sum += month[i]
    
    if res == 0:
        return day[(b-1)%7]

    res = (sum + b) % 7
    return day[res]

# 다른 풀이법
def solution(a, b):
    answer = 0
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    
    for i in range(a-1):
      answer += months[i]
    
    answer += b-1
    answer = answer%7
    
    return days[answer]
    
print(solution(1, 3))