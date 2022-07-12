import sys
sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
largest = -2160000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        # 행의 합
        sum1 += array[i][j]
        # 열의 합
        sum2 += array[j][i]
    if largest < sum1:
        largest = sum1
    if largest < sum2:
        largest = sum2 

sum1=sum2=0
for i in range(n):
    sum1 += array[i][i]
    sum2 += array[i][n-1-i]
if largest < sum1:
    largest = sum1
if largest < sum2:
    largest = sum2 

print(largest)