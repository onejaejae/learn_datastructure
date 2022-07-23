# import sys
# sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

n = int(input())
array = []
dic = dict()

for _  in range(n):
    array.append(input())

for _ in range(n-1):
    dic[input()] = 0

for x in array:
    if x not in dic:
        print(x)