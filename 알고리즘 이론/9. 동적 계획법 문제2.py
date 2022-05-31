# 백준 9461
def dp(num):
    cache = [0 for i in range(101)]
    
    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    for i in range(4, num+1):
        cache[ i] = cache[ i-3] + cache[ i-2]
    
    return cache[num]

print(dp(9))