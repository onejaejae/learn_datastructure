# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

# 나의 풀이
# n = int(input())
# count = 0
# 
# for i in range(2, n+1):
#     for j in range(2, i):
#         print(j)
#         if i % j == 0:
#             break
#     else: 
#         count+=1

#print(count)

# 해설 풀이
n = int(input())
count = 0
array = [0] * (n+1)

for i in range(2, n+1):
    if array[i] == 0:
        count += 1
        for j in range(i*2, n+1, i):
            array[j] = 1

print(count)