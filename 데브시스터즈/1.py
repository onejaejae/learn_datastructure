def solution(openA, closeB):
    answer = 0

    while openA:
        first = openA[0]
        close = closeB.pop(0)

        if first < close:
            while openA:
                if openA[0] < close:
                    openA.pop(0)
                else:
                    break
            answer += (close-first)
    return answer


print(solution([4, 7, 9, 16], [2, 5, 12, 14, 20]))