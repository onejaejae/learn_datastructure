import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(v):
    if v > n:
        for i in range(1,len(ch)):
            if ch[i] == 1:
                print(i,end="")
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)