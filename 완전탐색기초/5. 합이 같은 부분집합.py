import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(L, sum):
    if sum > tot // 2:
        return

    if L == n:
        if sum == tot - sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum)
    


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    tot = sum(a)
    DFS(0,0)
    print("NO")