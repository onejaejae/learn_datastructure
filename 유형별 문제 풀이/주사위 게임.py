import sys
sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

maximum = -21600000
n = int(input())
for _ in range(n):
    array = list(map(int, input().split()))
    array.sort()
    a,b,c = array

    if a == b and b == c:
        sum = 10000 + (a*1000)
    elif a == b or a == c:
        sum = 1000 + (a*100)
    elif b == c:
        sum = 1000 + (b*100)
    else:
        sum  = c * 100
    
    if maximum < sum:
        maximum = sum

print(maximum)