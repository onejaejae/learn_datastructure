import sys
sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

#나의 풀이
# n = int(input())
# array =input().split()
# sum_arr = list()

# 
#def digit_sum(x):
#    sum = 0
#    
#    for data in list(x):
#        sum += int(data)

#    return sum

#for i in range(n):
#    result = digit_sum(array[i])
#    sum_arr.append((result,i))

#b = sorted(sum_arr, key=lambda x: (-x[0], x[1]))
#print(array[b[0][1]])

# 해설 풀이
n = int(input())
array = list(map(int,input().split()))
sum_arr = list()

def degit_sum(x):
    sum = 0

    while x>0:
        sum += x%10
        x //= 10
    return sum

max = -2147000000
for x in array:
    tot = degit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)