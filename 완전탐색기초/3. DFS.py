import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2) # 왼쪽 자식 노드
        DFS((v*2) +1) # 오른쪽 자식 노드
        print(v, end=" ")  

if __name__ == "__main__":
    n = int(input())
    DFS(n)
