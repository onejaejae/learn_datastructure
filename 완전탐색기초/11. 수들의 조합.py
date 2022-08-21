# import sys
# sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(L,S):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for i in range(S, n):
            res[L] = arr[i]
            DFS(L+1,i+1)

if __name__ == "__main__":
    cnt = 0
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    res = [0] * k
    DFS(0,0)
    print(cnt)