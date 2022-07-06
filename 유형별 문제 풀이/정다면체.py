#import sys
#sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

n,m = map(int, input().split())
array = list(0 for i in range (n+m+1))

for i in range(1,n+1):
    for j in range(1,m+1):
        array[i+j] += 1

maxNumber = max(array)
for k in range(1, n+m+1):
    if array[k] == maxNumber:
        print(k, end=" ")