def solution(tasks):
    dic = dict()
    for x in tasks:
        dic[x] = dic.get(x, 0) + 1
    
    sum = 0
    tasks = list(set(tasks))
    for task in tasks:
        while dic[task] != 0:
            if dic[task] % 3 == 0:
                sum += dic[task] // 3 
                dic[task] = dic[task] % 3 
            elif dic[task] % 2 == 0:
                sum += dic[task] // 2 
                dic[task] = dic[task] % 2 
            else:
                sum += dic[task] // 3
                dic[task] = dic[task] % 3 

            
    return sum

print(solution([1, 1, 2, 3, 3,3,3,3, 2, 2]))