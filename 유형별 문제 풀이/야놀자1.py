from __future__ import print_function
import sys
sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

str = input()
array = []

p1, p2 = 0, 1
i = 0 
tmp = 0
sum = 0

while p2 < len(str):
    if str[p1] == str[p2]:
        p1 += 1
        p2 += 1
        
    else:
        array.append(str[i:p2])
        p1=p2
        p2+=1
        i=p1
array.append(str[i:p2])

max = -216000
for x in array:
    if max < len(x):
        max = len(x)


for y in array:
    if max > len(y):
        print(y, max - len(y))
        sum += max - len(y)


