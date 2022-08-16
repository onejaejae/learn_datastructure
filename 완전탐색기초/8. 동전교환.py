import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(L, sum):
    global res
    if L > res:
        return 
    if sum > m:
        return
    if m == sum:
        res = min(L, res)
    else:
        for i in range(len(arr)):
            DFS(L+1, sum + arr[i])


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    res = 2160000
    arr.sort(reverse=True)
    DFS(0, 0)
    print(res)
    