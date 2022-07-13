# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
array2 = [list(map(int , input().split())) for _ in range(m)]

for x in array2:
    a,b,c = x
    for i in range(c):
        if b == 0:
            data = array[a-1].pop(0)
            array[a-1].append(data)
        else:
            data = array[a-1].pop()
            array[a-1].insert(0, data)

p1, p2 = 0, n-1
tot = 0

for i in range(n):
    for j in range(p1, p2+1):
        tot += array[i][j]
    if n//2 <= i:
        p1 -= 1
        p2 += 1
       
    else:
        p1 += 1
        p2 -= 1
       

print(tot)
