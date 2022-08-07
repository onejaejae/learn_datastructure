def solution(levels):
    if len(levels) % 4 == 1 or len(levels) % 4 == 0:
        x = len(levels) // 4
    else:
        return -1
    
    return levels[-x]

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))