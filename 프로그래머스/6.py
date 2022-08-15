
def solution(order):
    answer = 0
    i = 1
    s = []

    while order:
        if i == order[0]:
            order.pop(0)
            i += 1
            answer += 1
        elif s != [] and s[-1] == order[0]:
            s.pop()
            order.pop(0)
            answer += 1
        elif i > len(order):
            break
        else:
            s.append(i)
            i += 1

    return answer

print(solution([5, 4, 3, 1, 2]))