def solution(numbers):
    res = 0
    for i in range(1, 10):
        if i not in numbers:
           res += i 
    return res

print(solution([1,2,3,4,6,7,8,0]))