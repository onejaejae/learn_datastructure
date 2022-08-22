import sys
sys.stdin = open("C:\workspaces\자료구조\넥슨\input.txt", "rt")
n, m = map(int, input().split())
arr = []
Max = -216000
for i in range(n):
    res = list(map(int, input().split()))
    arr.append(res)

for i in range(n):
    for j in range(n):
        res = arr[i][j]
        for k in range(1,m+1):
            left = j-k
            right = j+k
            up = i-k
            down = i+k

            if left >= 0:
                res += arr[i][left]
            if right < n:
                res += arr[i][right]
            if up >= 0:
                res += arr[up][j]
            if down < n:
                res += arr[down][j]
        Max = max(Max, res)

print(Max)