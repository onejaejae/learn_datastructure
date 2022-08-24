def solution(n):
    res = []
    sum = 0
    j=0

    while n > 0:
        res.append(n % 3)
        n //= 3

    for i in range(len(res)-1,-1,-1):
        if res[i] != 0:
            sum += (pow(3,j) * res[i])
        j+=1
    return sum
print(solution(125))