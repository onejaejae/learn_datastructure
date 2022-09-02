import sys
sys.stdin = open("C:\workspaces\자료구조\DFS, BFS 활용\input.txt", "rt")

def DFS(L):
    global res
    if L == n:
        cha = max(tot) - min(tot)      
        if res > cha:
            tmp = set()
            for x in tot:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            tot[i] += money[L]
            DFS(L+1)
            tot[i] -= money[L]
                



if __name__ == "__main__":
    n = int(input())
    money = []
    tot = [0] * 3
    res = 216000
    for _ in range(n):
        m =int(input())
        money.append(m)
    
    DFS(0)
    print(res)