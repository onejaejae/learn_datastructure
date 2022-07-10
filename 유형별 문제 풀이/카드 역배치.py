# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

array = list()
array.append(range(21))

for _ in range(10):
    a,b = map(int, input().split())
    size = (b-a+1) // 2
   
    for j in range(size):
        array[a+j], array[b-j] = array[b-j], array[a+j]

for k in range(1, len(array)):
    print(array[k], end=" ")