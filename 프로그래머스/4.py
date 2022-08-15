def solution(X, Y):
    res=[]
    X = list(X)
    Y = list(Y)
  
    for x in X:
        if x in Y:
            res.append(x)
            Y.remove(x)
    
    if res == []:
        return "-1"
    if res[0] == 0:
        return "0"
    res.sort(reverse=True)
    return ''.join(res)

print(solution("5525", "1255"))