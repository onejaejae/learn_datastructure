def solution(array, commands):
    answer = []

    for c in commands:
        i,j,k = c
        res = array[i-1:j]
        res.sort()
        answer.append(res[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))