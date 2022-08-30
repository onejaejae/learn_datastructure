# 나의 풀이
def solution(a, b):
    if b < a:
        a,b = b,a
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

# 최적 코드
def adder(a, b):
    return sum(range(min(a,b), max(a,b) + 1))

print(solution(5,3))