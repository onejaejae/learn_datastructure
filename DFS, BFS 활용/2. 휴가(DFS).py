# import sys
# sys.stdin = open("C:\workspaces\자료구조\DFS, BFS 활용\input.txt", "rt")

def DFS(L, sum):
    global max
    if L > n:
        return
    
    if L == n:
        if sum > max:
            max = sum
    else:
        DFS(L+days[L], sum + money[L])
        DFS(L+1, sum)



if __name__ == "__main__":
    n =  int(input())
    max = -216000
    days = []
    money = []
    
    for _ in range(n):
        d,m = map(int, input().split())
        days.append(d)
        money.append(m)
    
    DFS(0,0)
    print(max)