def solution(left, right):
    res = []
    
    for i in range(left, right+1):
        if i == 1:
            res.append(-1)
            continue

        cnt = 0
        for j in range(2, int(i**(1/2)) + 1):
            if i % j == 0:
                if j == i//j:
                    cnt += 1
                else:
                    cnt += 2
        
        if cnt % 2 == 0:
            res.append(i)
        else:
            res.append(i * -1)
    
    return sum(res)

print(solution(1,2))