import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

n,m = map(int, input().split())
res = []
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    i, j , dis = map(int, input().split())
    arr[i][j] = dis

for i in range(1, n+1):
    for j in range(1,n+1):
        print(arr[i][j], end=" ")
    print()
