def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
    return sum(absolutes)

print(solution([4, 7, 12], [True, False, True]))