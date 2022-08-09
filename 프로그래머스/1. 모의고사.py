def solution(answers):
    score = [0] * 3 
    a = [1,2,3,4,5]
    b= [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    for idx, value in enumerate(answers):
        if value == a[idx % len(a)]:
            score[0] += 1
        if value == b[idx % len(b)]:
            score[1] += 1
        if value == c[idx % len(c)]:
            score[2] += 1
    
    r = [i + 1 for i,v in enumerate(score) if max(score) == v]
    return r

print(solution([1,2,3,4,5]))