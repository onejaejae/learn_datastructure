# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")


n = int(input())
array = list(map(int,input().split()))

m = int(input())
array2 = list(map(int, input().split()))

new_array = []
p1,p2 = 0, 0

while p1 < n and p2 < m:
    if array[p1] > array2[p2]:
        new_array.append(array2[p2])
        p2 += 1
    else:
        new_array.append(array[p1])
        p1 += 1

if p1 < n:
    new_array = new_array + array[p1:]
elif p2 < m:
    new_array = new_array + array2[p2:]

print(new_array)