#import sys
#sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

n = int(input())

for _ in range(n):
    n,s,e,k = map(int, input().split())
    array = list(map(int, input().split()))

    new_array = array[s-1:e]
    new_array.sort()
    print(new_array[k-1])