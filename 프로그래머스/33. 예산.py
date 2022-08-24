def solution(d, budget):
    d.sort()
    cnt = 0
    for x in d:
        if budget - x >= 0:
            cnt +=1
            budget -= x
    return cnt

   
print(solution(	[2, 2, 3, 3], 10))