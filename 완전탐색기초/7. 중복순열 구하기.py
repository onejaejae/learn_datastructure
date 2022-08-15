import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(L):
    global cnt
    
    if L == m:
        for r in res:
            print(r, end=" ")
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)

if __name__ == "__main__":
    n,m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)