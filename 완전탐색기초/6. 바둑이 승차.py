import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(n, sum, tsum):
    global res

    if sum + (total - tsum) < res:
        return
    if sum > c:
        return

    if n == len(arr):
        res = max(res, sum)
    else:
        DFS(n+1, sum + arr[n], tsum + arr[n])
        DFS(n+1, sum, tsum + arr[n])


if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = []
    res = -216000
    for _ in range(n):
        arr.append(int(input()))
    total = sum(arr)
    DFS(0, 0, 0)
    print(res)