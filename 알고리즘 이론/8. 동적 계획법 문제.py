def dp(num):
    cache = [0 for i in range(num+1)]
    
    cache[1] = 1
    cache[2] = 2

    for i in range(3, num+1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[num] % 10007

num = int(input())
print(dp(num)) 