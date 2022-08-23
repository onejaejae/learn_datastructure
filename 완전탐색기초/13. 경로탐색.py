import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(L):
    global cnt
    if L == n:
        cnt +=1
    else:
        for i in range(2, n+1):
            if arr[L][i] == 1 and check[i] == 0:
                check[i] = 1
                DFS(i)
                check[i] = 0
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0] * (n+1) for _ in range(n+1)]
    check = [0] * (n+1)

    for i in range(m):
        i, j = map(int, input().split())
        arr[i][j] = 1
    cnt = 0
    DFS(1)
    print(cnt)