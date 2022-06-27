dic = dict()
n = int(input())

def piv(n):
    if n in dic:
        return dic[n]
    
    if n == 0:
        dic[0] = 0
        return dic[0]
    elif n == 1:
        dic[1] = 1
        return dic[1]
    else:
        dic[n] = piv(n-1) + piv(n-2)
        return dic[n]

print(piv(n))

