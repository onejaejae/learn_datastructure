def solution(begin, end):
    answer = [0] * 10

    for i in range(begin, end+1):
        for j in range(2, 11):
            if i * j <= 10:
                answer[(i*j) -1] = i
            else:
                break
    return answer

print(solution(1, 10))