# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

n = int(input())
array = list(map(int, input().split()))

def reverse(x):
    result = 0
    while x > 0:
        tot = x % 10
        x //= 10
        result = result * 10 + tot
    return result

def isPrime(x):
    if x == 1:
        return False

    # 절반까지만 돌아도 약수인지를 알 수 있다.
    for i in range(2, (x//2) + 1):
        if x % i == 0:
            return False
    # for-else문은 break, return 문도 포함
    else:
        return True

for x in array:
    result = reverse(x)
    if isPrime(result):
        print(result)
