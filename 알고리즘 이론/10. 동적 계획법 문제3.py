import sys
input = sys.stdin.readline

def dp(num):
    cache = [0 for i in range(1000001)]

    cache[1] = 1
    cache[2] = 2
    for i in range(3, num+1):
        #결과 값에만 나눠주는 게 아니라 반복문 안에서도 수시로 나머지 연산을 해 주어야 메모리 초과가 발생하지 않는다. 
        # (값이 int값을 초과하기 때문에 n = 1000000 일 경우 엄청나게 많은 메모리를 차지하게 된다.)
        cache[i] = (cache[i-1] + cache[i-2]) % 15746
 
    return cache[num]  % 15746

print(dp(int(input())))