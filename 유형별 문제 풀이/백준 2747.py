# 피보나치 수열의 점화식을 세운다.
# 재귀 함수를 이용해 문제를 풀 수 있는지 검토해야함
# 문제에서 N은 최대 45이다.

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

