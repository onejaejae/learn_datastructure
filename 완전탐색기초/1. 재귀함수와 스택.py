import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x)

if __name__=="__main__":
    n = int(input())
    DFS(n)
