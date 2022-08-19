def solution(n):
    res = [1,2]

    for i in range(2, n+1):
        res.append(res[i-2] + res[i-1])


    return res[n-1]


print(solution(5))