# https://needneo.tistory.com/92 

def solution(numbers):  
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    
    numbers = sorted(numbers, key=lambda x : x * 3, reverse=True)
    return str(int("".join(numbers)))


print(solution([999, 9, 998]))