# 나의 풀이
def solution(arr, divisor):
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    if answer == []:
        return [-1]
    
    return sorted(answer)

# 다른 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

print(solution([5, 9, 7, 10], 5))