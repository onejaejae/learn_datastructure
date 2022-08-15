import copy   

def solution(want, number, discount):
    dic = dict()
    cnt = 0
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        res = copy.deepcopy(dic)
        for j in range(i, i+10):
            if discount[j] in dic:
                res[discount[j]] -= 1

        r = list(res.values())
        for x in r:
            if x > 0:
                break
        else:
            cnt += 1
    return cnt


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))