from collections import deque

def solution(priorities, location):
    array = [(value, i) for i, value in enumerate(priorities)]
    array = deque(array)
    cnt = 0
    
    while True:
        cur = array.popleft()
        if any(cur[0] < x[0] for x in array):
            array.append(cur)
        else:
            cnt += 1
            if cur[1] == location:
                return cnt

print(solution([1, 1, 9, 1, 1, 1], 0))